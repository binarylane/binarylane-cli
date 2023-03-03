from __future__ import annotations

from typing import Any, List

import pytest

from binarylane.console import Context
from binarylane.console.commands import commands
from binarylane.console.printers import formatter


def ok_response_types() -> List[type]:
    types: List[type] = []
    for command_type in commands:
        types.append(command_type(Context()).command_runner.ok_response_type)
    return types


@pytest.fixture(params=ok_response_types())
def ok_response_type(request: pytest.FixtureRequest) -> Any:
    return request.param


def test_response_type(ok_response_type: type) -> None:
    assert formatter.check_response_type(ok_response_type), f"{ok_response_type} will not format correctly"
