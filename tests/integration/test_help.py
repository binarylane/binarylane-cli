from __future__ import annotations

import pytest
from pytest import CaptureFixture

from tests.integration.conftest import App

from binarylane.console.metadata import program_description


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
