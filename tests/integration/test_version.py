from __future__ import annotations

from _pytest.capture import CaptureFixture

from binarylane.console.app import App


def test_version(capsys: CaptureFixture[str]) -> None:
    runner = App()
    runner.run(["version"])

    captured = capsys.readouterr()
    assert "bl version" in captured.out
