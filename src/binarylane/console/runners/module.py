from __future__ import annotations

import importlib
import logging
from abc import abstractmethod
from typing import TYPE_CHECKING, List, Type

from binarylane.console.runners import Runner

if TYPE_CHECKING:
    from binarylane.console.runners.command import CommandRunner

logger = logging.getLogger(__name__)


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
    def command_runner_type(self) -> Type[CommandRunner]:
        """CommandRunner that will be executed by run()"""
        return importlib.import_module(f".{self.module_path}", package=__package__).Command

    @property
    def command_runner(self) -> CommandRunner:
        return self.command_runner_type(self)

    def run(self, args: List[str]) -> None:
        logger.debug("ModuleRunner for %s (%s). Received arguments: %s", self.name, self.module_path, args)
        self.command_runner.run(args)
