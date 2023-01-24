from __future__ import annotations

import pytest
from _pytest.capture import CaptureFixture

from tests.runner import TypeRunner

from binarylane.console.app import App
from binarylane.console.runners import Runner


def test_package_command_metavar(capsys: CaptureFixture[str]) -> None:
    runner = App()

    with pytest.raises(SystemExit) as exc:
        runner.run(["wrong"])
    assert exc.value.code == 2

    captured = capsys.readouterr()
    assert "\nbl: error: argument COMMAND: invalid choice: 'wrong'" in captured.err