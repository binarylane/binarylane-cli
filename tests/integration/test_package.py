from __future__ import annotations

import pytest
from _pytest.capture import CaptureFixture

from tests.runner import TypeRunner

from binarylane.console.commands import Size
from binarylane.console.runners import Runner


def test_package_command_metavar(capsys: CaptureFixture[str]) -> None:
    runner = TypeRunner[Runner](Size)

    with pytest.raises(SystemExit) as exc:
        runner.run(["wrong"])
    assert exc.value.code == 2

    captured = capsys.readouterr()
    assert "\ntest size: error: argument COMMAND: invalid choice: 'wrong'" in captured.err
