from __future__ import annotations

import importlib
import sys
from abc import ABC, abstractmethod
from argparse import SUPPRESS
from dataclasses import dataclass
from enum import Enum
from typing import ClassVar, List, NoReturn, Sequence, Type
from binarylane.pycompat.actions import BooleanOptionalAction

from binarylane.config import DefaultConfig, UserConfig

from binarylane.console.metadata import program_name
from binarylane.console.parser import Namespace, Parser


class Context(UserConfig):
    name: str = ""
    description: str = ""

    @property
    def prog(self) -> str:
        return f"{program_name()} {self.name}".rstrip()

    def configure(self, parser: Parser) -> None:
        default = DefaultConfig()
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


class ExitCode(int, Enum):
    ARGUMENT = 2  # ArgumentParser.error() uses this
    TOKEN = 3  # 401 Unauthorized response
    API = 4  # Did not understand API response


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

        self._parser.on_parse_args = self._context.add_commandline

    def configure(self, parser: Parser) -> None:
        """Subclasses add arguments to parser here"""

    def parse(self, args: Sequence[str]) -> Namespace:
        parsed = self._parser.parse(args)
        return parsed

    @abstractmethod
    def run(self, args: List[str]) -> None:
        """Subclasses implement their primary behaviour here"""

    @staticmethod
    def error(code: ExitCode, message: str) -> NoReturn:
        print(f"ERROR: {message}", file=sys.stderr)
        raise SystemExit(code.value)
