""" Contains methods for accessing vpc endpoints """
from __future__ import annotations

from typing import List, Type

from ...runners import ModuleRunner

__all__ = ["commands"]
commands: List[Type[ModuleRunner]] = []


def register_command(cls: ModuleRunner) -> ModuleRunner:
    commands.append(cls)
    return cls


@register_command
class VpcGet(ModuleRunner):
    """Runner for vpc_get API operation"""

    @property
    def name(self) -> str:
        return "get"

    @property
    def description(self) -> str:
        return "Fetch an Existing VPC"

    @property
    def module_path(self) -> str:
        return ".commands.vpc.vpc_get"


@register_command
class VpcUpdate(ModuleRunner):
    """Runner for vpc_update API operation"""

    @property
    def name(self) -> str:
        return "update"

    @property
    def description(self) -> str:
        return "Update an Existing VPC"

    @property
    def module_path(self) -> str:
        return ".commands.vpc.vpc_update"


@register_command
class VpcDelete(ModuleRunner):
    """Runner for vpc_delete API operation"""

    @property
    def name(self) -> str:
        return "delete"

    @property
    def description(self) -> str:
        return "Delete an Existing VPC"

    @property
    def module_path(self) -> str:
        return ".commands.vpc.vpc_delete"


@register_command
class VpcPatch(ModuleRunner):
    """Runner for vpc_patch API operation"""

    @property
    def name(self) -> str:
        return "patch"

    @property
    def description(self) -> str:
        return "Update an Existing VPC"

    @property
    def module_path(self) -> str:
        return ".commands.vpc.vpc_patch"


@register_command
class VpcList(ModuleRunner):
    """Runner for vpc_list API operation"""

    @property
    def name(self) -> str:
        return "list"

    @property
    def description(self) -> str:
        return "List All Existing VPCs"

    @property
    def module_path(self) -> str:
        return ".commands.vpc.vpc_list"


@register_command
class VpcCreate(ModuleRunner):
    """Runner for vpc_create API operation"""

    @property
    def name(self) -> str:
        return "create"

    @property
    def description(self) -> str:
        return "Create a New VPC"

    @property
    def module_path(self) -> str:
        return ".commands.vpc.vpc_create"


@register_command
class VpcMembers(ModuleRunner):
    """Runner for vpc_members API operation"""

    @property
    def name(self) -> str:
        return "members"

    @property
    def description(self) -> str:
        return "List All Members of an Existing VPC"

    @property
    def module_path(self) -> str:
        return ".commands.vpc.vpc_members"
