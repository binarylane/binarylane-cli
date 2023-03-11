from __future__ import annotations

from typing import List

import pytest

from tests.runner import TypeRunner

from binarylane.console.commands.api import descriptors
from binarylane.console.printers import formatter
from binarylane.console.runners.command import CommandRunner


def ok_response_types() -> List[type]:
    return [
        TypeRunner[CommandRunner](t.runner_type).test.ok_response_type
        for t in descriptors
        if issubclass(t.runner_type, CommandRunner)
    ]


@pytest.fixture(params=ok_response_types())
def ok_response_type(request: pytest.FixtureRequest) -> type:
    return request.param


def test_response_type(ok_response_type: type) -> None:
    assert formatter.check_response_type(ok_response_type), f"{ok_response_type} will not format correctly"
