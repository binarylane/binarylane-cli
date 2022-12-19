""" Contains methods for accessing action endpoints """
from __future__ import annotations

from typing import List, Type

from ...runner import ModuleRunner, Runner

__all__ = ["commands"]
commands: List[Type[Runner]] = []


def register_command(cls):
    commands.append(cls)
    return cls


@register_command
class ActionGet(ModuleRunner):
    """Runner for action_get API operation"""

    @property
    def name(self) -> str:
        return "get"

    @property
    def description(self) -> str:
        return "Fetch an Existing Action"

    @property
    def module_path(self) -> str:
        return ".commands.action.action_get"


@register_command
class ActionList(ModuleRunner):
    """Runner for action_list API operation"""

    @property
    def name(self) -> str:
        return "list"

    @property
    def description(self) -> str:
        return "List All Actions"

    @property
    def module_path(self) -> str:
        return ".commands.action.action_list"


@register_command
class ActionProceed(ModuleRunner):
    """Runner for action_proceed API operation"""

    @property
    def name(self) -> str:
        return "proceed"

    @property
    def description(self) -> str:
        return "Respond to a UserInteractionRequired Action"

    @property
    def module_path(self) -> str:
        return ".commands.action.action_proceed"
