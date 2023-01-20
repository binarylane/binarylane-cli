""" Contains methods for accessing domain endpoints """
from __future__ import annotations

from typing import List, Type

from binarylane.console.runners.module import ModuleRunner

__all__ = ["commands"]
commands: List[Type[ModuleRunner]] = []


def register_command(cls: Type[ModuleRunner]) -> Type[ModuleRunner]:
    commands.append(cls)
    return cls


@register_command
class DomainNameserversList(ModuleRunner):
    """Runner for domain_nameservers_list API operation"""

    @property
    def name(self) -> str:
        return "nameservers_list"

    @property
    def description(self) -> str:
        return "List All Public Nameservers"

    @property
    def module_path(self) -> str:
        return ".commands.domain.domain_nameservers_list"


@register_command
class DomainRefreshNameserverCache(ModuleRunner):
    """Runner for domain_refresh-nameserver-cache API operation"""

    @property
    def name(self) -> str:
        return "refresh-nameserver-cache"

    @property
    def description(self) -> str:
        return "Refresh Cached Nameserver Domain Records"

    @property
    def module_path(self) -> str:
        return ".commands.domain.domain_refresh_nameserver_cache"


@register_command
class DomainList(ModuleRunner):
    """Runner for domain_list API operation"""

    @property
    def name(self) -> str:
        return "list"

    @property
    def description(self) -> str:
        return "List All Domains"

    @property
    def module_path(self) -> str:
        return ".commands.domain.domain_list"


@register_command
class DomainCreate(ModuleRunner):
    """Runner for domain_create API operation"""

    @property
    def name(self) -> str:
        return "create"

    @property
    def description(self) -> str:
        return "Create a New Domain"

    @property
    def module_path(self) -> str:
        return ".commands.domain.domain_create"


@register_command
class DomainGet(ModuleRunner):
    """Runner for domain_get API operation"""

    @property
    def name(self) -> str:
        return "get"

    @property
    def description(self) -> str:
        return "Fetch an Existing Domain"

    @property
    def module_path(self) -> str:
        return ".commands.domain.domain_get"


@register_command
class DomainDelete(ModuleRunner):
    """Runner for domain_delete API operation"""

    @property
    def name(self) -> str:
        return "delete"

    @property
    def description(self) -> str:
        return "Delete an Existing Domain"

    @property
    def module_path(self) -> str:
        return ".commands.domain.domain_delete"


@register_command
class DomainRecordList(ModuleRunner):
    """Runner for domain_record_list API operation"""

    @property
    def name(self) -> str:
        return "record_list"

    @property
    def description(self) -> str:
        return "List All Domain Records for a Domain"

    @property
    def module_path(self) -> str:
        return ".commands.domain.domain_record_list"


@register_command
class DomainRecordCreate(ModuleRunner):
    """Runner for domain_record_create API operation"""

    @property
    def name(self) -> str:
        return "record_create"

    @property
    def description(self) -> str:
        return "Create a New Domain Record"

    @property
    def module_path(self) -> str:
        return ".commands.domain.domain_record_create"


@register_command
class DomainRecordGet(ModuleRunner):
    """Runner for domain_record_get API operation"""

    @property
    def name(self) -> str:
        return "record_get"

    @property
    def description(self) -> str:
        return "Fetch an Existing Domain Record"

    @property
    def module_path(self) -> str:
        return ".commands.domain.domain_record_get"


@register_command
class DomainRecordUpdate(ModuleRunner):
    """Runner for domain_record_update API operation"""

    @property
    def name(self) -> str:
        return "record_update"

    @property
    def description(self) -> str:
        return "Update an Existing Domain Record"

    @property
    def module_path(self) -> str:
        return ".commands.domain.domain_record_update"


@register_command
class DomainRecordDelete(ModuleRunner):
    """Runner for domain_record_delete API operation"""

    @property
    def name(self) -> str:
        return "record_delete"

    @property
    def description(self) -> str:
        return "Delete an Existing Domain Record"

    @property
    def module_path(self) -> str:
        return ".commands.domain.domain_record_delete"
