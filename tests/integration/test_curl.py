from __future__ import annotations

from typing import TYPE_CHECKING

from tests.runner import TypeRunner

from binarylane.console.commands.api import get_v2_sizes as size_list
from binarylane.console.runners.command import CommandRunner

if TYPE_CHECKING:
    from _pytest.capture import CaptureFixture


def test_curl_size_list(capsys: CaptureFixture[str]) -> None:
    runner = TypeRunner[CommandRunner](size_list.Command)
    runner.run(["--curl"])

    captured = capsys.readouterr()
    assert captured.out == (
        "curl --request GET 'https://api.binarylane.com.au/v2/sizes?page=1&per_page=25' "
        "--header 'Authorization: Bearer example_token'\n"
    )
