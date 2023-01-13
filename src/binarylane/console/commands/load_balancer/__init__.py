""" Contains methods for accessing load_balancer endpoints """
from __future__ import annotations

from typing import List, Type

from binarylane.console.runners import ModuleRunner

__all__ = ["commands"]
commands: List[Type[ModuleRunner]] = []


def register_command(cls: Type[ModuleRunner]) -> Type[ModuleRunner]:
    commands.append(cls)
    return cls


@register_command
class LoadBalancerGet(ModuleRunner):
    """Runner for load-balancer_get API operation"""

    @property
    def name(self) -> str:
        return "get"

    @property
    def description(self) -> str:
        return "Fetch an Existing Load Balancer"

    @property
    def module_path(self) -> str:
        return ".commands.load_balancer.load_balancer_get"


@register_command
class LoadBalancerUpdate(ModuleRunner):
    """Runner for load-balancer_update API operation"""

    @property
    def name(self) -> str:
        return "update"

    @property
    def description(self) -> str:
        return "Update an Existing Load Balancer"

    @property
    def module_path(self) -> str:
        return ".commands.load_balancer.load_balancer_update"


@register_command
class LoadBalancerDelete(ModuleRunner):
    """Runner for load-balancer_delete API operation"""

    @property
    def name(self) -> str:
        return "delete"

    @property
    def description(self) -> str:
        return "Cancel an Existing Load Balancer"

    @property
    def module_path(self) -> str:
        return ".commands.load_balancer.load_balancer_delete"


@register_command
class LoadBalancerList(ModuleRunner):
    """Runner for load-balancer_list API operation"""

    @property
    def name(self) -> str:
        return "list"

    @property
    def description(self) -> str:
        return "List all Load Balancers"

    @property
    def module_path(self) -> str:
        return ".commands.load_balancer.load_balancer_list"


@register_command
class LoadBalancerCreate(ModuleRunner):
    """Runner for load-balancer_create API operation"""

    @property
    def name(self) -> str:
        return "create"

    @property
    def description(self) -> str:
        return "Create a New Load Balancer"

    @property
    def module_path(self) -> str:
        return ".commands.load_balancer.load_balancer_create"


@register_command
class LoadBalancerAvailability(ModuleRunner):
    """Runner for load-balancer_availability API operation"""

    @property
    def name(self) -> str:
        return "availability"

    @property
    def description(self) -> str:
        return "Fetch Load Balancer Availability and Pricing"

    @property
    def module_path(self) -> str:
        return ".commands.load_balancer.load_balancer_availability"


@register_command
class LoadBalancerServerCreate(ModuleRunner):
    """Runner for load-balancer_server_create API operation"""

    @property
    def name(self) -> str:
        return "server_create"

    @property
    def description(self) -> str:
        return "Add Servers to an Existing Load Balancer"

    @property
    def module_path(self) -> str:
        return ".commands.load_balancer.load_balancer_server_create"


@register_command
class LoadBalancerServerDelete(ModuleRunner):
    """Runner for load-balancer_server_delete API operation"""

    @property
    def name(self) -> str:
        return "server_delete"

    @property
    def description(self) -> str:
        return "Remove Servers from an Existing Load Balancer"

    @property
    def module_path(self) -> str:
        return ".commands.load_balancer.load_balancer_server_delete"


@register_command
class LoadBalancerRuleCreate(ModuleRunner):
    """Runner for load-balancer_rule_create API operation"""

    @property
    def name(self) -> str:
        return "rule_create"

    @property
    def description(self) -> str:
        return "Add Forwarding Rules to an Existing Load Balancer"

    @property
    def module_path(self) -> str:
        return ".commands.load_balancer.load_balancer_rule_create"


@register_command
class LoadBalancerRuleDelete(ModuleRunner):
    """Runner for load-balancer_rule_delete API operation"""

    @property
    def name(self) -> str:
        return "rule_delete"

    @property
    def description(self) -> str:
        return "Remove Forwarding Rules from an Existing Load Balancer"

    @property
    def module_path(self) -> str:
        return ".commands.load_balancer.load_balancer_rule_delete"
