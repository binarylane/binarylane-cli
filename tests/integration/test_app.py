from __future__ import annotations

import pytest
from _pytest.capture import CaptureFixture

from binarylane.console.app import App


@pytest.fixture
def app() -> App:
    return App()


def test_app_program_name(app: App, capsys: CaptureFixture[str]) -> None:

    # for this to pass, the correct command names need to have been extracted
    with pytest.raises(SystemExit):
        app.run(["server", "kernel", "list"])

    captured = capsys.readouterr()
    assert "usage: bl server kernel list" in captured.err


def test_app_option_at_start(app: App) -> None:
    # Does not raise SystemExit:
    app.run(["--context", "bl", "server"])


def test_app_option_at_end(app: App) -> None:
    # Currently not supported
    with pytest.raises(SystemExit):
        app.run(["server", "--context", "bl"])


def test_app_invalid_root_command(app: App, capsys: CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit):
        app.run(["wrong"])

    captured = capsys.readouterr()
    assert "\nbl: error: argument COMMAND: invalid choice: 'wrong'" in captured.err


def test_app_invalid_sub_command(app: App, capsys: CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit):
        app.run(["server", "wrong"])

    captured = capsys.readouterr()
    assert "\nbl server: error: argument COMMAND: invalid choice: 'wrong'" in captured.err


def test_app_invalid_root_option(app: App, capsys: CaptureFixture[str]) -> None:

    with pytest.raises(SystemExit):
        app.run(["--wrong"])

    captured = capsys.readouterr()
    assert "\nbl: error: unrecognized arguments: --wrong" in captured.err


def test_app_invalid_sub_option(app: App, capsys: CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit):
        app.run(["server", "--wrong"])

    captured = capsys.readouterr()
    assert "\nbl server: error: unrecognized arguments: --wrong" in captured.err


def test_app_root_help(app: App, capsys: CaptureFixture[str]) -> None:
    app.run(["--help"])

    captured = capsys.readouterr()
    assert "Access server commands" in captured.out


def test_app_sub_help(app: App, capsys: CaptureFixture[str]) -> None:
    app.run(["server", "--help"])

    captured = capsys.readouterr()
    assert "usage: bl server" in captured.out
    assert "\nAccess server commands\n" in captured.out
