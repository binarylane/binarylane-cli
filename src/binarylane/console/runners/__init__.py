""" Runners handle the overall CLI behaviour - parse input, perform an action, and display result """
from __future__ import annotations

import re
import sys
from abc import ABC, abstractmethod
from typing import List, Optional


class Runner(ABC):
    """Abstract base class for all Runner implementations"""

    HELP = "--help"
    CHECK = "--blcli-check"
    _parent: Optional[Runner]

    def __init__(self, parent: Optional[Runner] = None) -> None:
        self._parent = parent

    @property
    def prog(self) -> str:
        """The 'program' name is used in help output to identify this runner"""
        return (self._parent.prog + " " if self._parent else "") + self.name

    @property
    @abstractmethod
    def name(self) -> str:
        """CLI name that is used to invoke the runner"""

    @property
    @abstractmethod
    def description(self) -> str:
        """Description of what this runner does"""

    def format_description(self) -> str:
        """Many API operation summaries are title-cased (like a headline), rather than as a sentence."""
        return re.sub(" ([A-Z])([a-z])", lambda m: " " + m.group(1).lower() + m.group(2), self.description)

    @abstractmethod
    def run(self, args: List[str]) -> None:
        """Subclasses implement their primary behaviour here"""

    def __call__(self, args: List[str]) -> None:
        self.run(args)

    @staticmethod
    def error(message: str) -> None:
        print("ERROR: ", message, file=sys.stderr)
        raise SystemExit(-1)
