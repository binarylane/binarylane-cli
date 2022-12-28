from typing import Any, Union

from ...client.api.account.account_invoice_get import sync_detailed
from ...client.client import Client
from ...client.models.invoice_response import InvoiceResponse
from ...client.models.problem_details import ProblemDetails
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "account_invoice_get"

    @property
    def description(self):
        return """Fetch an Invoice"""

    def configure(self, parser):
        """Add arguments for account_invoice_get"""
        parser.cli_argument(
            "invoice_id",
        )

    def request(
        self,
        invoice_id: int,
        client: Client,
    ) -> Union[Any, InvoiceResponse, ProblemDetails]:

        return sync_detailed(
            invoice_id=invoice_id,
            client=client,
        ).parsed
