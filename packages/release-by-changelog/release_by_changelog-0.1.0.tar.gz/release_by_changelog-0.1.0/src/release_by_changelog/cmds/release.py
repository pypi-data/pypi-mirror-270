import pathlib
import typing

import rich.panel
import rich.table
import typer

import release_by_changelog.exc
from release_by_changelog.app import app
from release_by_changelog.cmds._release import (
    _changelog_file,
    _last_changelog,
    _project,
    _release,
)

err_console = rich.console.Console(stderr=True)


@app.command()
def release(
    project: str = typer.Argument(help="Path or id on host.", envvar="CI_PROJECT_ID"),
    ref: str = typer.Argument(
        help="Can be a branch, tag, or commit SHA.",
        envvar="CI_COMMIT_SHA",
    ),
    changelog_path: typing.Annotated[
        pathlib.Path,
        typer.Option(help="Path to the changelog file."),
    ] = pathlib.Path("CHANGELOG.md"),
    host: typing.Annotated[
        str,
        typer.Option(
            help="URL of the GitLab instance.",
            envvar="CI_SERVER_HOST",
        ),
    ] = "gitlab.com",
    interact: bool = typer.Option(
        True,
        help="CLI ask for confirmation before creating the release. "
        "No interaction means automatic confirmation.",
    ),
    token: str = typer.Option(
        None,
        help="[red]Required[/red] for [yellow]user-based[/yellow] authentication.",
        envvar="PRIVATE_TOKEN",
    ),
    ci_job_token: str = typer.Option(
        None,
        help="[red]Required[/red] for [yellow]CI-based[/yellow] authentication.",
        envvar="CI_JOB_TOKEN",
    ),
) -> None:
    console = rich.console.Console()

    if not token and not ci_job_token:
        err_console.print(
            rich.panel.Panel(
                "You need to provide a PRIVATE_TOKEN or a CI_JOB_TOKEN",
                title="Error: Missing token",
                title_align="left",
                subtitle="release_by_changelog --help",
                subtitle_align="left",
                expand=False,
                border_style="red",
            )
        )
        raise typer.Exit(code=1)

    token = token or ci_job_token

    try:
        changelog_path = _changelog_file(
            changelog_path, token, host, project, ref, console
        )
    except release_by_changelog.exc.UnauthorizedError:
        err_console.print("Error: Unauthorized", style="bold red")
        raise typer.Exit(code=1)

    console.print(f"Processing [bold cyan]{changelog_path}[/bold cyan]")
    changelog_entry = _last_changelog(changelog_path)
    console.print(
        "[bold green]Found changelog entry:[/bold green] "
        f"[bold cyan]{changelog_entry.version}[/bold cyan]"
    )

    project_, project_name = _project(token, host, project, console)

    if interact:
        typer.confirm("Do you confirm release?", default=True, abort=True)

    console.print(
        f"Creating release [bold cyan]{changelog_entry.version}[/bold cyan] for "
        f"project [bold cyan]{project_name}[/bold cyan]"
    )
    try:
        result = _release(project_, changelog_entry, ref)
    except release_by_changelog.exc.UnauthorizedError:
        err_console.print("Error: Unauthorized", style="bold red")
        raise typer.Exit(code=1)
    except release_by_changelog.exc.ReleaseAlreadyExistError:
        err_console.print("Error: Release already exists", style="bold red")
        raise typer.Exit(code=1)
    console.print(f"Release created: {result}", style="bold green")


if __name__ == "__main__":
    release(
        project="1484",
        ref="main",
        changelog_path=pathlib.Path("test_dir/TEST_CHANGELOG.md"),
        host="lab.frogg.it",
        interact=True,
        token="glpat-nxkztk41T6-WDxfaifxs",
    )
