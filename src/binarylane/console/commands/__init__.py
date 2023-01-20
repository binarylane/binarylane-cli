""" Contains methods for accessing the API """
from __future__ import annotations

import importlib
from typing import List, Type

from binarylane.console.runners.package import PackageRunner

__all__ = ["commands"]
commands: List[Type[PackageRunner]] = []


def register_command(cls: Type[PackageRunner]) -> Type[PackageRunner]:
    commands.append(cls)
    return cls


@register_command
class Account(PackageRunner):
    """Runner for account API operations"""

    @property
    def package_name(self) -> str:
        return "account"

    @property
    def package_path(self) -> str:
        return f".commands.account"


@register_command
class Action(PackageRunner):
    """Runner for action API operations"""

    @property
    def package_name(self) -> str:
        return "action"

    @property
    def package_path(self) -> str:
        return f".commands.action"


@register_command
class Domain(PackageRunner):
    """Runner for domain API operations"""

    @property
    def package_name(self) -> str:
        return "domain"

    @property
    def package_path(self) -> str:
        return f".commands.domain"


@register_command
class Image(PackageRunner):
    """Runner for image API operations"""

    @property
    def package_name(self) -> str:
        return "image"

    @property
    def package_path(self) -> str:
        return f".commands.image"


@register_command
class LoadBalancer(PackageRunner):
    """Runner for load_balancer API operations"""

    @property
    def package_name(self) -> str:
        return "load-balancer"

    @property
    def package_path(self) -> str:
        return f".commands.load_balancer"


@register_command
class Region(PackageRunner):
    """Runner for region API operations"""

    @property
    def package_name(self) -> str:
        return "region"

    @property
    def package_path(self) -> str:
        return f".commands.region"


@register_command
class Server(PackageRunner):
    """Runner for server API operations"""

    @property
    def package_name(self) -> str:
        return "server"

    @property
    def package_path(self) -> str:
        return f".commands.server"


@register_command
class ServerAction(PackageRunner):
    """Runner for server_action API operations"""

    @property
    def package_name(self) -> str:
        return "server-action"

    @property
    def package_path(self) -> str:
        return f".commands.server_action"


@register_command
class Size(PackageRunner):
    """Runner for size API operations"""

    @property
    def package_name(self) -> str:
        return "size"

    @property
    def package_path(self) -> str:
        return f".commands.size"


@register_command
class Software(PackageRunner):
    """Runner for software API operations"""

    @property
    def package_name(self) -> str:
        return "software"

    @property
    def package_path(self) -> str:
        return f".commands.software"


@register_command
class SshKey(PackageRunner):
    """Runner for ssh_key API operations"""

    @property
    def package_name(self) -> str:
        return "ssh-key"

    @property
    def package_path(self) -> str:
        return f".commands.ssh_key"


@register_command
class Vpc(PackageRunner):
    """Runner for vpc API operations"""

    @property
    def package_name(self) -> str:
        return "vpc"

    @property
    def package_path(self) -> str:
        return f".commands.vpc"
