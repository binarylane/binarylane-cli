from __future__ import annotations

import importlib
import sys
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import ClassVar, List, Type


@dataclass
class Context:
    name: str
    description: str

    @property
    def prog(self) -> str:
        return f"bl {self.name}"


@dataclass
class Descriptor:
    module_path: str
    name: str
    description: str

    @property
    def runner_type(self) -> Type[Runner]:
        module = importlib.import_module("binarylane.console" + self.module_path)
        command_type = getattr(module, "Command", None)
        if command_type is None:
            raise RuntimeError(f"{module.__name__} does not contain Command class")
        return command_type


class Runner(ABC):
    HELP: ClassVar[str] = "--help"
    CHECK: ClassVar[str] = "--blcli-check"

    _context: Context

    def __init__(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def run(self, args: List[str]) -> None:
        """Subclasses implement their primary behaviour here"""

    @staticmethod
    def error(message: str) -> None:
        print("ERROR: ", message, file=sys.stderr)
        raise SystemExit(-1)
