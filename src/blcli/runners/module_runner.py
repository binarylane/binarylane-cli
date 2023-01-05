# pylint: disable=missing-module-docstring

import importlib
from abc import abstractmethod
from typing import List

from ..cli import debug
from .runner import Runner


class ModuleRunner(Runner):
    """ModuleRunner imports a runner from specified module."""

    @property
    def prog(self) -> str:
        return self.parent.prog if self.parent else ""

    @property
    @abstractmethod
    def module_path(self) -> str:
        """Path of python module containing runner to import during run()"""

    def run(self, args: List[str]) -> None:
        debug(f"ModuleRunner for {self.name} ({self.module_path}). Received arguments: {args}")
        cls = importlib.import_module(f".{self.module_path}", package=__package__).Command
        command = cls(self)
        command.run(args)
