from __future__ import annotations

from typing import Dict, Sequence

from binarylane.console.runners import Runner


class CommandNode:
    """CommandNode is used to represent all available runners in a tree.

    - Each node has 1..N  child nodes and/or runners (leaves).
    - A command like "server firewall list" is broken up into 1..N words ["server", "firewall", "list"]
    - The last word (e.g. "list") - identifies the corresponding runner leaf.
    - All proceeding words 1..(N-1) identify child nodes.
    """

    _command: str
    _word: str
    _nodes: Dict[str, CommandNode]
    _runners: Dict[str, Runner]

    def __init__(self, command: str = "") -> None:
        self._command = command
        self._word = command.split(" ")[-1]
        self._nodes = {}
        self._runners = {}

    def add(self, words: Sequence[str], runner: Runner) -> None:
        if not words:
            raise ValueError("words cannot be empty")

        if len(words) == 1:
            return self._add_runner(words[0], runner)

        return self._add_node(words[0]).add(words[1:], runner)

    def _add_runner(self, word: str, runner: Runner) -> None:
        self._runners[word] = runner

    def _add_node(self, word: str) -> CommandNode:
        if word in self._nodes:
            return self._nodes[word]
        child = CommandNode(f"{self._command} {word}".lstrip())
        self._nodes[word] = child
        return child

    def has_runner(self, word: str) -> bool:
        return word in self._runners

    def get_runner(self, word: str) -> Runner:
        return self._runners[word]

    def has_node(self, word: str) -> bool:
        return word in self._nodes

    def get_node(self, word: str) -> CommandNode:
        return self._nodes[word]

    @property
    def command(self) -> str:
        return self._command

    @property
    def children(self) -> Sequence[str]:
        return sorted(list(self._nodes.keys()) + list(self._runners.keys()))

    def get_child_description(self, word: str) -> str:
        return f"Access {word} commands" if not self.has_runner(word) else self.get_runner(word).description

    def __repr__(self) -> str:
        nodes = list(self._nodes.keys())
        runners = list(self._runners.keys())
        return f"CommandNode(command='{self._command}', nodes={nodes}, runners={runners})"
