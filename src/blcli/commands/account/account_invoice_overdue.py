from typing import Any, List, Union

from ...client.api.account.account_invoice_overdue import sync_detailed
from ...client.client import Client
from ...client.models.unpaid_failed_invoices_response import UnpaidFailedInvoicesResponse
from ...runners import ListRunner


class Command(ListRunner):
    @property
    def default_format(self) -> List[str]:
        return [
            "invoice_id",
            "invoice_number",
            "amount",
            "tax",
            "created",
            "date_due",
            "date_overdue",
            "paid",
            "refunded",
        ]

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
