""" Contains methods for accessing size endpoints """
from __future__ import annotations

from typing import List, Type

from ...runner import ModuleRunner, Runner

__all__ = ["commands"]
commands: List[Type[Runner]] = []


def register_command(cls):
    commands.append(cls)
    return cls


@register_command
class SizeList(ModuleRunner):
    """Runner for size_list API operation"""

    @property
    def name(self) -> str:
        return "list"

    @property
    def description(self) -> str:
        return "List All Available Sizes"

    @property
    def module_path(self) -> str:
        return ".commands.size.size_list"
