from __future__ import annotations

from typing import Generic, List, Type, TypeVar

from binarylane.config import Option

from binarylane.console import Context
from binarylane.console.runners import Runner

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
        super().__init__(Context())
        # Use default config, plus a token
        self.context.add_option(Option.API_TOKEN, "example_token")

        self._test = runner_type(self.context)

    @property
    def test(self) -> T:
        return self._test

    @property
    def name(self) -> str:
        return "test"

    @property
    def description(self) -> str:
        return "test"

    def run(self, args: List[str]) -> None:
        assert self._test is not None
        self._test.run(args)
