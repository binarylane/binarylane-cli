from __future__ import annotations

import importlib
import logging
from typing import List, Type

from binarylane.console.app.lazy_runner import LazyRunner
from binarylane.console.runners import Context, Runner

logger = logging.getLogger(__name__)


class LazyLoader(Runner):
    """ProxyRunner lazy imports a command from specified module."""

    def __init__(self, context: Context, module_path: str, name: str, description: str) -> None:
        super().__init__(context)

        self._module_path = module_path
        self._name = name
        self._description = description

    @property
    def prog(self) -> str:
        return self._context.prog if self._context else ""

    @property
    def module_path(self) -> str:
        return self._module_path

    @property
    def name(self) -> str:
        return self._name

    @property
    def description(self) -> str:
        return self._description

    @property
    def runner_type(self) -> Type[LazyRunner]:
        """Runner that will be executed by run()"""
        return importlib.import_module(f".{self.module_path}", package=__package__).Command

    @property
    def runner(self) -> Runner:
        return self.runner_type(self)

    def run(self, args: List[str]) -> None:
        logger.debug("ProxyRunner for %s (%s). Received arguments: %s", self.name, self.module_path, args)
        self.runner.run(args)
