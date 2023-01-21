from __future__ import annotations

import pytest
from _pytest.capture import CaptureFixture

from tests.runner import TypeRunner

from binarylane.console.commands.size import size_list
from binarylane.console.runners.command import CommandRunner


def test_list_invalid_format_value(capsys: CaptureFixture[str]) -> None:
    runner = TypeRunner[CommandRunner](size_list.Command)

    with pytest.raises(SystemExit):
        runner.run(["--format", "wrong"])

    captured = capsys.readouterr()
    assert "invalid --format value: 'wrong'" in captured.err
