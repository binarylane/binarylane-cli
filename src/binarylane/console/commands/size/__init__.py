""" Contains methods for accessing size endpoints """
from __future__ import annotations

from typing import List, Type

from binarylane.console.runners import ModuleRunner

__all__ = ["commands"]
commands: List[Type[ModuleRunner]] = []


def register_command(cls: Type[ModuleRunner]) -> Type[ModuleRunner]:
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
