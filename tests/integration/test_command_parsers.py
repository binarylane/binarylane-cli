from __future__ import annotations

from typing import Any, List, Type

import pytest

from binarylane.console.commands import commands
from binarylane.console.parsers.argument import CommandArgument
from binarylane.console.runners import CommandRunner, Runner


def get_all_command_runners() -> List[Type[CommandRunner]]:
    types = []
    for command_type in commands:
        command = command_type()
        for item in command.module_runners:
            types.append(item.command_runner_type)
    return types


@pytest.fixture(params=get_all_command_runners())
def command_runner(request: pytest.FixtureRequest) -> Any:
    return request.param


@pytest.fixture
def test_runner() -> Runner:
    class TestRunner(Runner):
        @property
        def name(self) -> str:
            return "test"

        @property
        def description(self) -> str:
            return "test"

        def run(self, args: List[str]) -> None:
            pass

    return TestRunner()


def test_command_parser(command_runner: Type[CommandRunner], test_runner: Runner) -> None:
    CommandArgument.raise_on_unsupported = True
    command_runner(test_runner)
