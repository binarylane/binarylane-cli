from __future__ import annotations

from typing import Any, List, Type

import pytest

from tests.runner import TypeRunner

from binarylane.console.commands.api import commands
from binarylane.console.parser import Attribute
from binarylane.console.runners.command import CommandRunner


def get_all_command_runners() -> List[Type[CommandRunner]]:
    return [t.runner_type for t in commands if issubclass(t.runner_type, CommandRunner)]


@pytest.fixture(params=get_all_command_runners())
def command_runner(request: pytest.FixtureRequest) -> Any:
    return request.param


def test_command_parser(command_runner: Type[CommandRunner]) -> None:
    Attribute.raise_on_unsupported = True

    runner = TypeRunner(command_runner)
    runner.run([CommandRunner.CHECK])


def test_command_descriptions() -> None:
    for descriptor in commands:
        assert descriptor.description, f"{descriptor.name} does not have a description"
