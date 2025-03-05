from __future__ import annotations

from typing import TYPE_CHECKING

from binarylane.console.app import App

if TYPE_CHECKING:
    from _pytest.capture import CaptureFixture


def test_version(capsys: CaptureFixture[str]) -> None:
    runner = App()
    runner.run(["version"])

    captured = capsys.readouterr()
    assert "bl version" in captured.out
