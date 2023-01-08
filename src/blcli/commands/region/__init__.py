""" Contains methods for accessing region endpoints """
from __future__ import annotations

from typing import List, Type

from ...runners import ModuleRunner

__all__ = ["commands"]
commands: List[Type[ModuleRunner]] = []


def register_command(cls: ModuleRunner) -> ModuleRunner:
    commands.append(cls)
    return cls


@register_command
class RegionList(ModuleRunner):
    """Runner for region_list API operation"""

    @property
    def name(self) -> str:
        return "list"

    @property
    def description(self) -> str:
        return "List all Regions"

    @property
    def module_path(self) -> str:
        return ".commands.region.region_list"
