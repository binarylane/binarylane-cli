""" Contains methods for accessing account endpoints """
from __future__ import annotations

from typing import List, Type

from ...runners import ModuleRunner, Runner

__all__ = ["commands"]
commands: List[Type[Runner]] = []


def register_command(cls):
    commands.append(cls)
    return cls


@register_command
class AccountGet(ModuleRunner):
    """Runner for account_get API operation"""

    @property
    def name(self) -> str:
        return "get"

    @property
    def description(self) -> str:
        return "Fetch Information About the Current Account"

    @property
    def module_path(self) -> str:
        return ".commands.account.account_get"


@register_command
class AccountBalance(ModuleRunner):
    """Runner for account_balance API operation"""

    @property
    def name(self) -> str:
        return "balance"

    @property
    def description(self) -> str:
        return "Fetch Current Balance Information"

    @property
    def module_path(self) -> str:
        return ".commands.account.account_balance"


@register_command
class AccountInvoiceGet(ModuleRunner):
    """Runner for account_invoice_get API operation"""

    @property
    def name(self) -> str:
        return "invoice_get"

    @property
    def description(self) -> str:
        return "Fetch an Invoice"

    @property
    def module_path(self) -> str:
        return ".commands.account.account_invoice_get"


@register_command
class AccountInvoiceList(ModuleRunner):
    """Runner for account_invoice_list API operation"""

    @property
    def name(self) -> str:
        return "invoice_list"

    @property
    def description(self) -> str:
        return "Fetch Invoices"

    @property
    def module_path(self) -> str:
        return ".commands.account.account_invoice_list"


@register_command
class AccountInvoiceOverdue(ModuleRunner):
    """Runner for account_invoice_overdue API operation"""

    @property
    def name(self) -> str:
        return "invoice_overdue"

    @property
    def description(self) -> str:
        return "Fetch Unpaid Failed Invoices"

    @property
    def module_path(self) -> str:
        return ".commands.account.account_invoice_overdue"
