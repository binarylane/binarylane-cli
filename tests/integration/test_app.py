from __future__ import annotations

import pytest
from _pytest.capture import CaptureFixture

from binarylane.console.app import App


def test_app_program_name(capsys: CaptureFixture[str]) -> None:
    runner = App()

    # for this to pass, the correct command names need to have been extracted
    with pytest.raises(SystemExit):
        runner.run(["server", "kernel", "list"])

    captured = capsys.readouterr()
    assert "usage: bl server kernel list" in captured.err
