from __future__ import annotations

import contextlib
import functools
import http
import os
import pathlib
import re
import typing

import typer

if typing.TYPE_CHECKING:
    import rich.console

import gitlab.v4.objects

import release_by_changelog.exc

regex: typing.Final = re.compile(
    r"^## \[(?P<version>(?P<major>0|[1-9]\d*)\.(?P<minor>0|[1-9]\d*)\.(?P<patch>0|[1-9]"
    r"\d*)(?:-(?P<prerelease>(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*"
    r"|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+(?P<buildmetadata>[0-9a-zA-Z-]+(?:\.[0-9a-zA"
    r"-Z-]+)*))?)\]"
)


def _extract_last_version(f: typing.TextIO) -> str:
    for lines in f:
        matches = regex.finditer(lines)
        try:
            match = next(matches)
        except StopIteration:
            continue
        return match.group("version")
    raise ValueError("No changelog entry found")


def _extract_body(f: typing.TextIO) -> str:
    body = []
    for lines in f:
        matches = regex.finditer(lines)
        with contextlib.suppress(StopIteration):
            next(matches)
            break

        body.append(lines)
    return "".join(body)


class ChangelogEntry(typing.NamedTuple):
    version: str
    body: str


def _last_changelog(changelog_path: pathlib.Path) -> ChangelogEntry:
    """Extract the last changelog entry from the changelog file."""
    with changelog_path.open() as f:
        version = _extract_last_version(f)
        body = _extract_body(f)
    return ChangelogEntry(version=version, body=body)


@functools.cache
def _project(
    token: str,
    host: str,
    project: str,
    console: rich.console.Console,
) -> tuple[gitlab.v4.objects.Project, str]:
    console.print(
        f"Retrieving project [bold cyan]{project}[/bold cyan] from "
        f"[bold cyan]{host}[/bold cyan]"
    )
    url = f"https://{host}"
    gl = gitlab.Gitlab(url=url, oauth_token=token)
    try:
        project_ = gl.projects.get(project)
    except gitlab.GitlabAuthenticationError as e:
        if e.response_code == http.HTTPStatus.UNAUTHORIZED:
            raise release_by_changelog.exc.UnauthorizedError from e
        raise e
    project_name = f"{project_.namespace.get('full_path')}/{project_.name}"
    console.print(
        f"[bold green]Project found:[/bold green] [bold cyan]{project_name}[bold cyan]"
    )
    return project_, project_name


def _release(
    project: gitlab.v4.objects.Project,
    changelog_entry: ChangelogEntry,
    ref: str,
) -> str:
    data = {
        "ref": ref,
        "name": changelog_entry.version,
        "tag_name": changelog_entry.version,
        "description": changelog_entry.body,
    }
    try:
        project.releases.create(data)
    except gitlab.GitlabAuthenticationError as e:
        if e.response_code == http.HTTPStatus.UNAUTHORIZED:
            raise release_by_changelog.exc.UnauthorizedError from e
        raise e
    except gitlab.GitlabCreateError as e:
        if e.response_code == http.HTTPStatus.CONFLICT:
            raise release_by_changelog.exc.ReleaseAlreadyExistError from e
        raise e
    return changelog_entry.version


def _get_remote_changelog_file(
    changelog_path: pathlib.Path,
    console: rich.console.Console,
    project_: gitlab.v4.objects.Project,
    ref: str,
) -> gitlab.v4.objects.ProjectFile:
    try:
        changelog_file: gitlab.v4.objects.ProjectFile = project_.files.get(
            file_path=str(changelog_path), ref=ref
        )
    except gitlab.GitlabGetError as e:
        if e.response_code == http.HTTPStatus.NOT_FOUND:
            console.print(
                f"[bold red]Changelog file {changelog_path} not found in the remote "
                f"project files[/bold red]"
            )
            raise typer.Exit(code=1)
        raise e
    console.print(
        f"[bold cyan]{changelog_path}[/bold cyan] [bold green]found in the remote "
        f"project files[/bold green]"
    )
    return changelog_file


def _save_remote_changelog_file(
    changelog_file: gitlab.v4.objects.ProjectFile, changelog_path: pathlib.Path
) -> pathlib.Path:
    """
    Save the remote changelog file to a temporary file.

    :raises NotImplementedError: If the OS is not supported.
    """
    if os.name == "posix":
        tmp_file = pathlib.Path(f"/tmp/{changelog_path.name}")
    elif os.name == "nt":
        temp_path = pathlib.Path(os.environ["Temp"])
        tmp_file = temp_path / changelog_path.name
    else:
        raise NotImplementedError(f"OS {os.name} not supported")
    tmp_file.write_bytes(changelog_file.decode())
    return tmp_file


def _changelog_file(
    changelog_path: pathlib.Path,
    token: str,
    host: str,
    project: str,
    ref: str,
    console: rich.console.Console,
) -> pathlib.Path:
    """
    Find usable changelog file path.

    If the changelog file is not found locally, it will look for it in the remote
    project files.

    :raises NotImplementedError: If the OS is not supported.
    """
    console.print(f"Look for local [bold cyan]{changelog_path}[/bold cyan]")
    if changelog_path.exists():
        console.print(
            f"[bold green]Found local[/bold green] "
            f"[bold cyan]{changelog_path}[/bold cyan]"
        )
        return changelog_path

    console.print(
        f"[yellow]Local [bold cyan]{changelog_path}[/bold cyan] file not found, looking"
        " for file in the remote project files[/yellow]"
    )
    project_, _ = _project(
        token,
        host,
        project,
        console,
    )

    changelog_file = _get_remote_changelog_file(changelog_path, console, project_, ref)
    tmp_file = _save_remote_changelog_file(changelog_file, changelog_path)
    return tmp_file
