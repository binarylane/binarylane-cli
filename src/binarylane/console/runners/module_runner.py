from __future__ import annotations

import importlib
from abc import abstractmethod
from typing import TYPE_CHECKING, List

from binarylane.console.cli import debug
from binarylane.console.runners.runner import Runner

if TYPE_CHECKING:
    from binarylane.console.runners.command_runner import CommandRunner


class ModuleRunner(Runner):
    """ModuleRunner imports a runner from specified module."""

    @property
    def prog(self) -> str:
        return self._parent.prog if self._parent else ""

    @property
    @abstractmethod
    def module_path(self) -> str:
        """Path of python module containing runner to import during run()"""

    @property
    def command_runner(self) -> CommandRunner:
        """CommandRunner that will be executed by run()"""
        cls = importlib.import_module(f".{self.module_path}", package=__package__).Command
        return cls(self)

    def run(self, args: List[str]) -> None:
        debug(f"ModuleRunner for {self.name} ({self.module_path}). Received arguments: {args}")
        self.command_runner.run(args)
