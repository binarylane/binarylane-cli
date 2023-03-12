from __future__ import annotations

import os
from argparse import Namespace
from pathlib import Path
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
        super().__init__(Context("type", ""))
        # Use default config, plus a token
        commandline = Namespace()
        commandline.api_token = "example_token"
        self._context.initialize(commandline=commandline, config_file=Path(os.path.devnull))

        self._test = runner_type(self._context)

    @property
    def test(self) -> T:
        return self._test

    def run(self, args: List[str]) -> None:
        assert self._test is not None
        self._test.run(args)
