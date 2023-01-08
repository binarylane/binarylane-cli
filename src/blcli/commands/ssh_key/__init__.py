""" Contains methods for accessing ssh_key endpoints """
from __future__ import annotations

from typing import List, Type

from ...runners import ModuleRunner

__all__ = ["commands"]
commands: List[Type[ModuleRunner]] = []


def register_command(cls: ModuleRunner) -> ModuleRunner:
    commands.append(cls)
    return cls


@register_command
class SshKeyGet(ModuleRunner):
    """Runner for ssh-key_get API operation"""

    @property
    def name(self) -> str:
        return "get"

    @property
    def description(self) -> str:
        return "Fetch an Existing SSH Key"

    @property
    def module_path(self) -> str:
        return ".commands.ssh_key.ssh_key_get"


@register_command
class SshKeyUpdate(ModuleRunner):
    """Runner for ssh-key_update API operation"""

    @property
    def name(self) -> str:
        return "update"

    @property
    def description(self) -> str:
        return "Update an Existing SSH Key"

    @property
    def module_path(self) -> str:
        return ".commands.ssh_key.ssh_key_update"


@register_command
class SshKeyDelete(ModuleRunner):
    """Runner for ssh-key_delete API operation"""

    @property
    def name(self) -> str:
        return "delete"

    @property
    def description(self) -> str:
        return "Delete an Existing SSH Key"

    @property
    def module_path(self) -> str:
        return ".commands.ssh_key.ssh_key_delete"


@register_command
class SshKeyList(ModuleRunner):
    """Runner for ssh-key_list API operation"""

    @property
    def name(self) -> str:
        return "list"

    @property
    def description(self) -> str:
        return "List All SSH Keys"

    @property
    def module_path(self) -> str:
        return ".commands.ssh_key.ssh_key_list"


@register_command
class SshKeyCreate(ModuleRunner):
    """Runner for ssh-key_create API operation"""

    @property
    def name(self) -> str:
        return "create"

    @property
    def description(self) -> str:
        return "Add a New SSH Key"

    @property
    def module_path(self) -> str:
        return ".commands.ssh_key.ssh_key_create"
