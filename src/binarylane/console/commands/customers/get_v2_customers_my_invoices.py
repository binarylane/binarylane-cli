from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Dict, List, Optional, Tuple, Union

from binarylane.api.customers.get_v2_customers_my_invoices import sync_detailed
from binarylane.models.invoices_response import InvoicesResponse
from binarylane.models.links import Links

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import Mapping
from binarylane.console.runners.list import ListRunner


class CommandRequest:
    pass


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
            "tax_code": """The tax code that was applied to transactions on this invoice.""",
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
    def name(self) -> str:
        return "list"

    @property
    def description(self) -> str:
        return """Fetch Invoices"""

    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/Customers/paths/~1v2~1customers~1my~1invoices/get"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)
        return mapping

    @property
    def ok_response_type(self) -> type:
        return InvoicesResponse

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[None, InvoicesResponse]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.OK: InvoicesResponse
        # HTTPStatus.UNAUTHORIZED: Any
        page = 0
        per_page = 25
        has_next = True
        response: Optional[InvoicesResponse] = None

        while has_next:
            page += 1
            page_response = sync_detailed(
                client=client,
                page=page,
                per_page=per_page,
            )

            status_code = page_response.status_code
            if status_code != 200:
                return status_code, page_response.parsed

            assert isinstance(page_response.parsed, InvoicesResponse)
            has_next = isinstance(page_response.parsed.links, Links) and isinstance(
                page_response.parsed.links.pages.next_, str
            )
            if not response:
                response = page_response.parsed
            else:
                response.invoices += page_response.parsed.invoices

        return status_code, response
