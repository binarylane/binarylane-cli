from typing import Any, Dict, List, Union

from ...client.api.account.account_invoice_list import sync_detailed
from ...client.client import Client
from ...client.models.invoices_response import InvoicesResponse
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
    def fields(self) -> Dict[str, str]:
        return {
            "invoice_id": """The ID of the invoice.""",
            "invoice_number": """The invoice number for this invoice.""",
            "amount": """The amount of the invoice in AU$.""",
            "tax_code": """""",
            "tax": """The amount of tax (if any) that was charged on the transactions on this invoice.""",
            "created": """The date in ISO8601 format this invoice was created.""",
            "date_due": """The date in ISO8601 format this invoice is due for payment.""",
            "date_overdue": """The date in ISO8601 format this invoice is considered overdue.""",
            "paid": """If this is true the invoice has been paid.""",
            "refunded": """If this is true the payment for this invoice has been refunded.""",
            "invoice_items": """The individual items that make up invoice.""",
            "reference": """The reference for this invoice. If this invoice is for a single service this may identify the service, otherwise it will be the account reference.""",
            "payment_failure_count": """If this is included it indicates the number of failed attempts at processing payment for this invoice that have occurred.""",
            "invoice_download_url": """The download URL for the rendered version of the invoice.""",
        }

    @property
    def name(self):
        return "account_invoice_list"

    @property
    def description(self):
        return """Fetch Invoices"""

    def configure(self, parser):
        """Add arguments for account_invoice_list"""

    def request(
        self,
        client: Client,
    ) -> Union[Any, InvoicesResponse]:

        page = 0
        per_page = 25
        has_next = True
        response: InvoicesResponse = None

        while has_next:
            page += 1
            page_response = sync_detailed(
                client=client,
                page=page,
                per_page=per_page,
            )

            if page_response.status_code != 200:
                return page_response.parsed

            has_next = page_response.parsed.links and page_response.parsed.links.pages.next_
            if not response:
                response = page_response.parsed
            else:
                response.invoices += page_response.parsed.invoices

        return response
