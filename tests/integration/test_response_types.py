from typing import Any, List

import pytest

from blcli.commands import commands
from blcli.printers import formatter


def ok_response_types() -> List[Any]:
    types = []
    for command_type in commands:
        command = command_type()
        for item in command.module_runners:
            types.append(item.command_runner.ok_response_type)
    return types


@pytest.fixture(params=ok_response_types())
def ok_response_type(request: pytest.FixtureRequest) -> Any:
    return request.param


def test_response_type(ok_response_type: Any) -> None:
    assert formatter.check_response_type(ok_response_type), f"{ok_response_type} will not format correctly"
