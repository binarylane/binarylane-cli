from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from pytest import CaptureFixture

from binarylane.console.metadata import program_description

if TYPE_CHECKING:
    from tests.integration.conftest import App


def test_app_root_help(app: App, capsys: CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit):
        app.run(["--help"])

    captured = capsys.readouterr()
    assert program_description() in captured.out
    assert "Access server commands" in captured.out


def test_app_sub_help(app: App, capsys: CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit):
        app.run(["server", "--help"])

    captured = capsys.readouterr()
    assert "usage: bl server" in captured.out
    assert "\nAccess server commands\n" in captured.out


def test_required_argument_help(app: App, capsys: CaptureFixture[str]) -> None:
    # This command has required arguments, but `--help` should be shown regardless
    with pytest.raises(SystemExit):
        app.run(["server", "create", "--help"])

    captured = capsys.readouterr()
    assert "\nArguments:\n" in captured.out
    assert "\nParameters:\n" in captured.out


def test_help_with_percent_in_description(app: App, capsys: CaptureFixture[str]) -> None:
    # Help text containing "100%" should not cause argparse format string errors
    # The % character must be escaped as %% to prevent interpretation as format specifier
    with pytest.raises(SystemExit):
        app.run(["server", "alert", "get", "--help"])

    captured = capsys.readouterr()
    assert "usage: bl server alert get" in captured.out
    assert "100%" in captured.out
