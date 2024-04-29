import collections.abc

import click.testing
import pytest


@pytest.mark.usefixtures("successful_gitlab_interaction")
def test_release(
    app: collections.abc.Callable[[list[str]], click.testing.Result],
) -> None:
    result = app(
        ["--changelog-path", "FILE", "--token", "TOKEN", "--host", "HOST", "3", "main"]
    )
    assert result.exit_code == 0, result.stdout
    assert "Look for local FILE" in result.output
    assert (
        "Local FILE file not found, looking for file in the remote project files"
        in result.output
    )
    assert "Retrieving project 3 from HOST" in result.output
    assert "Project found: diaspora/Diaspora Project Site" in result.output
    assert "FILE found in the remote project files" in result.output
    assert "Found changelog entry: 1.0.0" in result.output
    assert (
        "Creating release 1.0.0 for project diaspora/Diaspora Project Site"
        in result.output
    )
    assert "Release created: 1.0.0" in result.output
