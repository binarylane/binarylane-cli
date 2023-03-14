from __future__ import annotations

import importlib
import sys
from abc import ABC, abstractmethod
from argparse import SUPPRESS
from dataclasses import dataclass
from typing import ClassVar, List, Sequence, Type
from binarylane.console.metadata import program_name
from binarylane.pycompat.actions import BooleanOptionalAction

from binarylane.config import Config

from binarylane.console.parser import Namespace, Parser


class Context(Config):
    name: str
    description: str

    def __init__(self, name: str = "", description: str = "") -> None:
        super().__init__(default_source=True)
        self.name = name
        self.description = description

    @property
    def prog(self) -> str:
        return f"{program_name()} {self.name}".rstrip()

    def configure(self, parser: Parser) -> None:
        default = Config()
        config_section = default.config_section

        parser.add_argument(
            "--context", metavar="NAME", help=f'Name of authentication context to use (default: "{config_section}")'
        )
        parser.add_argument("--api-token", metavar="VALUE", help="API token to use with BinaryLane API")
        parser.add_argument("--api-url", metavar="URL", help=SUPPRESS)
        parser.add_argument("--api-development", action=BooleanOptionalAction, help=SUPPRESS)

        # Undocumented for now due to poor help formatting
        parser.add_argument("-c", dest="context", help=SUPPRESS)
        parser.add_argument("-t", dest="api_token", help=SUPPRESS)


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
    HELP_DESCRIPTION: ClassVar[str] = "Display command options and descriptions"
    CHECK: ClassVar[str] = "--blcli-check"

    _context: Context
    _parser: Parser

    def __init__(self, context: Context) -> None:
        self._parser = Parser(context.prog, context.description)
        self._parser.add_argument("--help", help=self.HELP_DESCRIPTION, action="help")

        self._context = context
        self._context.configure(self._parser)
        self.configure(self._parser)

    def configure(self, parser: Parser) -> None:
        """Subclasses add arguments to parser here"""

    def parse(self, args: Sequence[str]) -> Namespace:
        parsed = self._parser.parse(args)
        self._context.initialize(commandline=parsed)
        return parsed

    @abstractmethod
    def run(self, args: List[str]) -> None:
        """Subclasses implement their primary behaviour here"""

    @staticmethod
    def error(message: str) -> None:
        print("ERROR: ", message, file=sys.stderr)
        raise SystemExit(-1)
