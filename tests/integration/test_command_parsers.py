from __future__ import annotations

from typing import Any, List, Type

import pytest

from tests.runner import TypeRunner

from binarylane.console.commands.api import commands
from binarylane.console.parser import Attribute
from binarylane.console.runners.command import CommandRunner


def get_all_command_runners() -> List[Type[CommandRunner]]:
    types: List[Type[CommandRunner]] = []
    for command_type in commands:
        types.append(command_type().command_runner_type)
    return types


@pytest.fixture(params=get_all_command_runners())
def command_runner(request: pytest.FixtureRequest) -> Any:
    return request.param


def test_command_parser(command_runner: Type[CommandRunner]) -> None:
    Attribute.raise_on_unsupported = True

    runner = TypeRunner(command_runner)
    assert runner.test.description, f"{type(runner.test)} does not have a description"
    runner.run([CommandRunner.CHECK])
