from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.runner import TypeRunner

from binarylane.console.commands.api import get_v2_sizes as size_list
from binarylane.console.runners.command import CommandRunner

if TYPE_CHECKING:
    from _pytest.capture import CaptureFixture


def test_list_invalid_format_value(capsys: CaptureFixture[str]) -> None:
    runner = TypeRunner[CommandRunner](size_list.Command)

    with pytest.raises(SystemExit):
        runner.run(["--format", "wrong"])

    captured = capsys.readouterr()
    assert "invalid --format value: 'wrong'" in captured.err
