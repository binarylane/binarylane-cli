from typing import Any, Union

from ...client.api.account.account_invoice_overdue import sync_detailed
from ...client.client import Client
from ...client.models.unpaid_failed_invoices_response import UnpaidFailedInvoicesResponse
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "account_invoice_overdue"

    @property
    def description(self):
        return """Fetch Unpaid Failed Invoices"""

    def configure(self, parser):
        """Add arguments for account_invoice_overdue"""

    def request(
        self,
        client: Client,
    ) -> Union[Any, UnpaidFailedInvoicesResponse]:

        return sync_detailed(
            client=client,
        ).parsed
