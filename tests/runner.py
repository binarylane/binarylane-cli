from __future__ import annotations

from argparse import Namespace
from typing import Generic, List, Type, TypeVar

from binarylane.console.runners import Context, Runner

T = TypeVar("T", bound=Runner)


class TypeRunner(Runner, Generic[T]):
    """TypeRunner is used as parent (root) runner for runner being tested.

    The constructor accepts type (class) of Runner, whic is instantiated and
    available via the `test` property.

    Most runners do not function correctly as a root runner, so should be
    "wrapped" in TypeRunner to match normal runtime conditions.
    """

    _test: T

    def __init__(self, runner_type: Type[T]) -> None:
        super().__init__(Context(config_file=None))
        # Use default config, plus a token
        commandline = Namespace()
        commandline.api_token = "example_token"
        self._context.add_commandline(commandline)

        self._test = runner_type(self._context)

    @property
    def test(self) -> T:
        return self._test

    def run(self, args: List[str]) -> None:
        assert self._test is not None
        self._test.run(args)
