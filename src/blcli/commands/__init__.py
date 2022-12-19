""" Contains methods for accessing the API """
from __future__ import annotations

import importlib
from typing import List, Type

from ..runner import PackageRunner, Runner

__all__ = ["commands"]
commands: List[Type[Runner]] = []


def register_command(cls: Type[Runner]) -> Type[Runner]:
    commands.append(cls)
    return cls


@register_command
class Account(PackageRunner):
    """Runner for account API operations"""

    @property
    def name(self) -> str:
        return "account"

    @property
    def description(self) -> str:
        return f"Access {self.name} commands"

    @property
    def package_path(self) -> str:
        return f".commands.account"


@register_command
class Action(PackageRunner):
    """Runner for action API operations"""

    @property
    def name(self) -> str:
        return "action"

    @property
    def description(self) -> str:
        return f"Access {self.name} commands"

    @property
    def package_path(self) -> str:
        return f".commands.action"


@register_command
class Domain(PackageRunner):
    """Runner for domain API operations"""

    @property
    def name(self) -> str:
        return "domain"

    @property
    def description(self) -> str:
        return f"Access {self.name} commands"

    @property
    def package_path(self) -> str:
        return f".commands.domain"


@register_command
class Image(PackageRunner):
    """Runner for image API operations"""

    @property
    def name(self) -> str:
        return "image"

    @property
    def description(self) -> str:
        return f"Access {self.name} commands"

    @property
    def package_path(self) -> str:
        return f".commands.image"


@register_command
class LoadBalancer(PackageRunner):
    """Runner for load_balancer API operations"""

    @property
    def name(self) -> str:
        return "load-balancer"

    @property
    def description(self) -> str:
        return f"Access {self.name} commands"

    @property
    def package_path(self) -> str:
        return f".commands.load_balancer"


@register_command
class Region(PackageRunner):
    """Runner for region API operations"""

    @property
    def name(self) -> str:
        return "region"

    @property
    def description(self) -> str:
        return f"Access {self.name} commands"

    @property
    def package_path(self) -> str:
        return f".commands.region"


@register_command
class Server(PackageRunner):
    """Runner for server API operations"""

    @property
    def name(self) -> str:
        return "server"

    @property
    def description(self) -> str:
        return f"Access {self.name} commands"

    @property
    def package_path(self) -> str:
        return f".commands.server"


@register_command
class ServerAction(PackageRunner):
    """Runner for server_action API operations"""

    @property
    def name(self) -> str:
        return "server-action"

    @property
    def description(self) -> str:
        return f"Access {self.name} commands"

    @property
    def package_path(self) -> str:
        return f".commands.server_action"


@register_command
class Size(PackageRunner):
    """Runner for size API operations"""

    @property
    def name(self) -> str:
        return "size"

    @property
    def description(self) -> str:
        return f"Access {self.name} commands"

    @property
    def package_path(self) -> str:
        return f".commands.size"


@register_command
class Software(PackageRunner):
    """Runner for software API operations"""

    @property
    def name(self) -> str:
        return "software"

    @property
    def description(self) -> str:
        return f"Access {self.name} commands"

    @property
    def package_path(self) -> str:
        return f".commands.software"


@register_command
class SshKey(PackageRunner):
    """Runner for ssh_key API operations"""

    @property
    def name(self) -> str:
        return "ssh-key"

    @property
    def description(self) -> str:
        return f"Access {self.name} commands"

    @property
    def package_path(self) -> str:
        return f".commands.ssh_key"


@register_command
class Vpc(PackageRunner):
    """Runner for vpc API operations"""

    @property
    def name(self) -> str:
        return "vpc"

    @property
    def description(self) -> str:
        return f"Access {self.name} commands"

    @property
    def package_path(self) -> str:
        return f".commands.vpc"
