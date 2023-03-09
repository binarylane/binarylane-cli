from __future__ import annotations

import importlib
import logging
from argparse import SUPPRESS
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Sequence

from binarylane.console.app.lazy_loader import LazyLoader
from binarylane.console.parser import Mapping, Parser
from binarylane.console.runners import Runner

logger = logging.getLogger(__name__)


class CommandNode:
    """CommandNode is used to represent all available runners in a tree.

    Each node has a mapping of word to child nodes and/or runners (terminating leaves). Command parsing is implemented
    by processing arguments left-to-right, descending the tree until either a runner is selected or available arguments
    are exhausted, in which case a help message is displayed based on the selected node.
    """

    full_name: str
    name: str
    children: Dict[str, CommandNode]
    runners: Dict[str, Runner]

    def __init__(self, full_name: str = "") -> None:
        self.full_name = full_name
        self.name = full_name.split(" ")[-1]
        self.children = {}
        self.runners = {}

    def add_runner(self, runner: Runner) -> None:
        self.runners[runner.name.split(" ")[-1]] = runner

    def has_runner(self, name: str) -> bool:
        return name in self.runners

    def get_runner(self, name: str) -> Runner:
        return self.runners[name]

    def has_child(self, name: str) -> bool:
        return name in self.children

    def get_child(self, name: str) -> CommandNode:
        return self.children[name]

    def get_or_add_child(self, name: str) -> CommandNode:
        if name in self.children:
            return self.children[name]
        child = CommandNode(f"{self.full_name} {name}".lstrip())
        self.children[name] = child
        return child

    def get_names(self) -> Sequence[str]:
        return sorted(list(self.children.keys()) + list(self.runners.keys()))

    def get_description(self, name: str) -> str:
        return f"Access {name} commands" if not self.has_runner(name) else self.get_runner(name).description

    def __repr__(self) -> str:
        children = list(self.children.keys())
        runners = list(self.runners.keys())
        return f"CommandGroup(full_name='{self.full_name}', children={children}, runners={runners})"


@dataclass
class AppRequest:
    command: List[str]


class App(Runner):
    """
    AppRunner is the 'root' runner for the application. In normal usage, all command line arguments are passed
    directly to run(). Apart from global flags, the primary function of this class is to invoke the
    appropriate runner for the supplied arguments.
    """

    parser: Parser
    command_tree: CommandNode

    def __init__(self, parent: Optional[Runner] = None) -> None:
        super().__init__(parent)
        self.command_tree = CommandNode()

        # Add each runner into our command tree
        for runner in self.runners:
            child = self.command_tree
            for word in runner.name.split(" ")[:-1]:
                child = child.get_or_add_child(word)
            child.add_runner(runner)

    @property
    def prog(self) -> str:
        return self.parser.prog

    @property
    def name(self) -> str:
        return "bl"

    @property
    def description(self) -> str:
        return "bl is a command-line interface for the BinaryLane API"

    @property
    def runners(self) -> Sequence[Runner]:
        return [cls(self) for cls in importlib.import_module("..commands", package=__package__).commands] + [
            LazyLoader(self, ".app.configure", "configure", "Configure access to BinaryLane API"),
            LazyLoader(self, ".app.version", "version", "Show the current version"),
        ]

    def configure(self) -> None:
        # Add COMMAND argument:
        mapping = self.parser.set_mapping(Mapping(AppRequest))
        mapping.add_primitive("command", List[Any], option_name=None, required=True, description=SUPPRESS)

        # Add global options:
        options = self.parser.add_argument_group(title="Options")
        options.add_argument("--help", help="Display available commands and descriptions", action="help")
        options.add_argument("--context", help=SUPPRESS)  # for test_app.py ; --context will be implemented later

    def update_parser(self, full_name: str) -> None:
        self.parser.prog = f"{self.name} {full_name}"
        self.parser.usage = f"{self.parser.prog} [OPTIONS] COMMAND"
        self.parser.description = f"Access {full_name} commands"

    def parse_command(self, args: List[str]) -> None:
        # Helper to check if word is an option (as opposed to positional argument)
        def is_option(word: str) -> bool:
            return word.startswith("-")

        # STEP 1: pop args[0] to descend command_tree until we find a runner to execute, or run out of non-option args
        node = self.command_tree
        while len(args) and not is_option(args[0]):
            name = args.pop(0)

            # Check name is valid (identifies a runner or child node):
            if name not in node.get_names():
                choices = ", ".join(f"'{name}'" for name in node.get_names())
                self.parser.error(f"argument COMMAND: invalid choice: '{name}' (choose from {choices})")

            # If we have found a runner, we are done
            if node.has_runner(name):
                return node.get_runner(name).run(args)

            # Otherwise, continue descent
            node = node.get_child(name)
            self.update_parser(node.full_name)

        # STEP 2: runner was not selected. If args contains anything other than HELP, there are invalid option(s)
        if len(args) and self.HELP not in args:
            self.parser.error(f"unrecognized arguments: {' '.join([word for word in args if is_option(word)])}")

        # STEP 3: Parsing has terminated at a node with no remaining args, so display the node's commands
        command_descriptions = {name: node.get_description(name) for name in node.get_names()}
        self.parser.add_group_help(title="Available Commands", entries=command_descriptions)
        return self.parser.print_help()

    def run(self, args: List[str]) -> None:
        # Allowing doing `bl help command [subcommand...]` instead of --help
        if args and args[0] == "help":
            args = args[1:] + [self.HELP]

        # Setup parser
        self.parser = Parser(self.name, self.description)
        self.configure()

        # We need to hide the --help parameter from argparse, so that we can pass it to a subrunner
        # rather than displaying our own help.
        extra: List[str] = []
        if self.HELP in args:
            args.remove(self.HELP)
            extra += [self.HELP]

        # If CHECK is requested, remove from args and execute it after ensuring parse_args() does not fail
        check = False
        if Runner.CHECK in args:
            args.remove(Runner.CHECK)
            check = True

        # Parse args
        parsed = self.parser.parse(args)
        if check:
            for runner in self.runners:
                runner.run([Runner.CHECK])
            return
        self.parse_command(list(parsed.mapped_object.command) + extra)
