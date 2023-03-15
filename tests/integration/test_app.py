from __future__ import annotations

import pytest
from _pytest.capture import CaptureFixture

from tests.integration.conftest import App, AppWithContext


def test_app_program_name(app: App, capsys: CaptureFixture[str]) -> None:
    # for this to pass, the correct command names need to have been extracted
    with pytest.raises(SystemExit):
        app.run(["server", "kernel", "list"])

    captured = capsys.readouterr()
    assert "usage: bl server kernel list" in captured.err


def test_app_option_at_start(app: AppWithContext) -> None:
    app.run(["--context", "foo", "server"])
    assert app.get_context().config_section == "foo"


def test_app_option_at_end(app: AppWithContext) -> None:
    app.run(["server", "--context", "foo"])
    assert app.get_context().config_section == "foo"


def test_app_option_after_command(app: AppWithContext) -> None:
    app.run(["server", "list", "--context", "foo", "--curl"])
    assert app.get_context().config_section == "foo"


def test_app_option_before_and_after_command(app: AppWithContext) -> None:
    app.run(["--api-token", "test_token", "server", "list", "--context", "foo", "--curl"])
    assert app.get_context().config_section == "foo"
    assert app.get_context().api_token == "test_token"


def test_app_option_after_command_overwrites_before_command(app: AppWithContext) -> None:
    app.run(["--context", "before", "server", "list", "--context", "after", "--curl"])
    assert app.get_context().config_section == "after"


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
