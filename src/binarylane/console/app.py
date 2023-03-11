from __future__ import annotations

import logging
from argparse import SUPPRESS
from dataclasses import dataclass
from typing import Any, Dict, Iterator, List, Optional, Union

from binarylane.console.commands import descriptors
from binarylane.console.parser import Mapping, Namespace, Parser
from binarylane.console.runners import Context, Descriptor, Runner

logger = logging.getLogger(__name__)

Command = Union["Node", Descriptor]


@dataclass
class AppRequest:
    command: List[str]


class App:
    """
    App is the 'root' runner for the application. In normal usage, all command line arguments are passed directly
    to run(). The primary function of this class is to invoke the appropriate runner for the supplied arguments.
    """

    _context: Context
    _parser: Parser
    _tree: Node

    def __init__(self) -> None:
        self._context = Context("bl", "bl is a command-line interface for the BinaryLane API")

        # Add each descriptor into our tree
        self._tree = Node()
        for descriptor in dict(sorted({d.name: d for d in descriptors}.items())).values():
            self._tree.add(descriptor)

        # Setup parser
        self._parser = Parser(self._context.name, self._context.description)
        self.configure()

    # Helper to update context + parser usage strings
    def _update_context(self, source: Command) -> None:
        self._context.name = source.name
        self._context.description = source.description

        self._parser.prog = f"bl {source.name}"
        self._parser.usage = f"{self._parser.prog} [OPTIONS] COMMAND"
        self._parser.description = f"Access {source.name} commands"

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

        # STEP 1: pop args[0] and descend command tree until we find a runner to execute, or run out of non-option args
        node = self._tree
        while len(args) and not is_option(args[0]):
            word = args.pop(0)
            child = node.get(word)

            # Check word is valid (identifies a child node or runner):
            if child is None:
                choices = ", ".join(f"'{word}'" for word in node)
                self._parser.error(f"argument COMMAND: invalid choice: '{word}' (choose from {choices})")

            # Update context
            self._update_context(child)

            # If we have found a descriptor, we are done
            if isinstance(child, Descriptor):
                return child.runner_type(self._context).run(args)

            # Otherwise, continue descent
            node = child

        # STEP 2: runner was not selected. If args contains anything other than HELP, there are invalid option(s)
        if len(args) and Runner.HELP not in args:
            self._parser.error(f"unrecognized arguments: {' '.join([word for word in args if is_option(word)])}")

        # STEP 3: Parsing has terminated at a node with no remaining args, so display the node's commands
        command_descriptions = {word: node[word].description for word in node}
        self._parser.add_group_help(title="Available Commands", entries=command_descriptions)
        return self._parser.print_help()

    def run(self, args: List[str]) -> None:
        # If CHECK is requested, skip parsing and execute all runners with CHECK instead:
        if args == [Runner.CHECK]:
            for descriptor in descriptors:
                self._update_context(descriptor)
                descriptor.runner_type(self._context).run([Runner.CHECK])
            return

        # Allowing doing `bl help command [subcommand...]` instead of --help
        if args and args[0] == "help":
            args = args[1:] + [Runner.HELP]

        # Move --help parameter to end of arguments, so that it is passed on to requested command
        if Runner.HELP in args:
            args += [args.pop(args.index(Runner.HELP))]

        parsed = self._parser.parse(args)
        self.process(parsed)


class Node:
    """Node is used to represent all available command descriptors as a tree structure.

    - Each node has 1..N  child nodes (branches) and/or descriptors (leaves).
    - A command like "server firewall list" is broken up into 1..N words ["server", "firewall", "list"]
    - The last word (e.g. "list") - identifies the corresponding descriptor leaf.
    - All proceeding words 1..(N-1) identify child nodes.
    """

    name: str
    description: str
    _children: Dict[str, Command]

    def __init__(self, name: str = "") -> None:
        self.name = name
        self.description = f"Access {name} commands"
        self._children = {}

    def __iter__(self) -> Iterator[str]:
        return self._children.__iter__()

    def get(self, word: str) -> Optional[Command]:
        return self._children.get(word)

    def __getitem__(self, word: str) -> Command:
        return self._children[word]

    def add(self, descriptor: Descriptor, words: Optional[List[str]] = None) -> None:
        if words is None:
            words = descriptor.name.split(" ")

        word = words.pop(0)
        if not words:
            self._children[word] = descriptor
            return

        child = self._children.get(word)
        if isinstance(child, Descriptor):
            raise RuntimeError("Descriptor cannot have same name as Node")
        if child is None:
            child = self._children[word] = Node(f"{self.name} {word}".lstrip())
        child.add(descriptor, words)
