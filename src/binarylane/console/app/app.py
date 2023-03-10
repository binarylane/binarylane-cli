from __future__ import annotations

import importlib
import logging
from argparse import SUPPRESS
from dataclasses import dataclass
from typing import Any, List, Optional, Sequence

from binarylane.console.app.command_node import CommandNode
from binarylane.console.runners.lazy_loader import LazyLoader
from binarylane.console.parser import Mapping, Namespace, Parser
from binarylane.console.runners import Runner

logger = logging.getLogger(__name__)


@dataclass
class AppRequest:
    command: List[str]


class App(Runner):
    """
    AppRunner is the 'root' runner for the application. In normal usage, all command line arguments are passed
    directly to run(). Apart from global flags, the primary function of this class is to invoke the
    appropriate runner for the supplied arguments.
    """

    _parser: Parser
    _root_node: CommandNode

    def __init__(self, parent: Optional[Runner] = None) -> None:
        super().__init__(parent)
        self._root_node = CommandNode()

        # Add each runner into our command tree
        for runner in self._runners:
            self._root_node.add(runner.name.split(" "), runner)

        # Setup parser
        self._parser = Parser(self.name, self.description)
        self.configure()

    @property
    def prog(self) -> str:
        return self._parser.prog

    @property
    def name(self) -> str:
        return "bl"

    @property
    def description(self) -> str:
        return "bl is a command-line interface for the BinaryLane API"

    @property
    def _runners(self) -> Sequence[Runner]:
        return [cls(self) for cls in importlib.import_module("..commands", package=__package__).commands] + [
            LazyLoader(self, "..commands.configure", "configure", "Configure access to BinaryLane API"),
            LazyLoader(self, "..commands.version", "version", "Show the current version"),
        ]

    def configure(self) -> None:
        # Add COMMAND argument:
        mapping = self._parser.set_mapping(Mapping(AppRequest))
        mapping.add_primitive("command", List[Any], option_name=None, required=True, description=SUPPRESS)

        # Add global options:
        options = self._parser.add_argument_group(title="Options")
        options.add_argument("--help", help="Display command options and descriptions", action="store_true")
        options.add_argument("--context", help=SUPPRESS)  # for test_app.py ; --context will be implemented later

    def process(self, parsed: Namespace) -> None:
        args: List[str] = parsed.mapped_object.command

        # Helper to check if word is an option (as opposed to positional argument)
        def is_option(word: str) -> bool:
            return word.startswith("-")

        # Helper to update parser usage strings
        def update_parser(command: str) -> None:
            self._parser.prog = f"{self.name} {command}"
            self._parser.usage = f"{self._parser.prog} [OPTIONS] COMMAND"
            self._parser.description = f"Access {command} commands"

        # STEP 1: pop args[0] and descend command tree until we find a runner to execute, or run out of non-option args
        node = self._root_node
        while len(args) and not is_option(args[0]):
            word = args.pop(0)

            # Check word is valid (identifies a child node or runner):
            if word not in node.children:
                choices = ", ".join(f"'{word}'" for word in node.children)
                self._parser.error(f"argument COMMAND: invalid choice: '{word}' (choose from {choices})")

            # If we have found a runner, we are done
            if node.has_runner(word):
                return node.get_runner(word).run(args)

            # Otherwise, continue descent
            node = node.get_node(word)
            update_parser(node.command)

        # STEP 2: runner was not selected. If args contains anything other than HELP, there are invalid option(s)
        if len(args) and self.HELP not in args:
            self._parser.error(f"unrecognized arguments: {' '.join([word for word in args if is_option(word)])}")

        # STEP 3: Parsing has terminated at a node with no remaining args, so display the node's commands
        command_descriptions = {word: node.get_child_description(word) for word in node.children}
        self._parser.add_group_help(title="Available Commands", entries=command_descriptions)
        return self._parser.print_help()

    def run(self, args: List[str]) -> None:
        # If CHECK is requested, skip parsing and execute all runners with CHECK instead:
        if args == [Runner.CHECK]:
            for runner in self._runners:
                runner.run([Runner.CHECK])
            return

        # Allowing doing `bl help command [subcommand...]` instead of --help
        if args and args[0] == "help":
            args = args[1:] + [self.HELP]

        # Move --help parameter to end of arguments, so that it is passed on to requested command
        if self.HELP in args:
            args += [args.pop(args.index(self.HELP))]

        parsed = self._parser.parse(args)
        self.process(parsed)
