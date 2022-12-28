""" Contains methods for accessing software endpoints """
from __future__ import annotations

from typing import List, Type

from ...runners import ModuleRunner, Runner

__all__ = ["commands"]
commands: List[Type[Runner]] = []


def register_command(cls):
    commands.append(cls)
    return cls


@register_command
class SoftwareGet(ModuleRunner):
    """Runner for software_get API operation"""

    @property
    def name(self) -> str:
        return "get"

    @property
    def description(self) -> str:
        return "Fetch Existing Software"

    @property
    def module_path(self) -> str:
        return ".commands.software.software_get"


@register_command
class SoftwareList(ModuleRunner):
    """Runner for software_list API operation"""

    @property
    def name(self) -> str:
        return "list"

    @property
    def description(self) -> str:
        return "List All Available Software"

    @property
    def module_path(self) -> str:
        return ".commands.software.software_list"


@register_command
class SoftwareOperatingSystem(ModuleRunner):
    """Runner for software_operating-system API operation"""

    @property
    def name(self) -> str:
        return "operating-system"

    @property
    def description(self) -> str:
        return "List All Available Software for an Existing Operating System"

    @property
    def module_path(self) -> str:
        return ".commands.software.software_operating_system"
