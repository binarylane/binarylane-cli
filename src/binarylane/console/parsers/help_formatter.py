from __future__ import annotations

import argparse
import re
import textwrap
import typing
from typing import Iterable, Optional


class CommandHelpFormatter(argparse.HelpFormatter):
    """Modified HelpFormatter with following changes:
    - preserves newlines, with text wrapping on each line
    - hides common options in displayed usage
    - converts markdown enum table to something readable in terminal
    """

    _markdown_matcher = re.compile(r"^\n*(\|.*\|)\n(\| --.* \|)\n((\|.*\|\n)*)\s$")

    def _split_lines(self, text: str, width: int) -> typing.List[str]:
        """Returns the provided text, split into multiple lines of the specified width"""

        markdown = self._markdown_matcher.match(text)
        if markdown:
            text = "One of the following values:\n" + "\n".join(
                ["  " + item.strip(" |").replace(" | ", " - ") for item in markdown.group(3).splitlines()]
            )

        return [text for text in text.splitlines() for text in textwrap.wrap(text, width)]

    def add_usage(
        self,
        usage: Optional[str],
        actions: Iterable[argparse.Action],
        groups: Iterable[argparse._ArgumentGroup],
        prefix: Optional[str] = None,
    ) -> None:
        actions = [argparse.Action(["OPTIONS"], "")] + [
            action for action in actions if not action.dest.startswith("runner_")
        ]
        super().add_usage(usage, actions, groups, prefix)
