from __future__ import annotations

from typing import Generic, List, Type, TypeVar

from binarylane.console.config import Config
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
        super().__init__(None)
        self._test = runner_type(self)

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

        # Use a stock config
        config = getattr(self._test, "_config", None)
        if isinstance(config, Config):
            config.api_token = "example_token"

        self._test.run(args)
