from __future__ import annotations

from http import HTTPStatus
from typing import Tuple, Union

from binarylane.api.account.account_invoice_get import sync_detailed
from binarylane.client import Client
from binarylane.models.invoice_response import InvoiceResponse
from binarylane.models.problem_details import ProblemDetails

from binarylane.console.parsers import CommandParser
from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "get"

    @property
    def description(self) -> str:
        return """Fetch an Invoice"""

    def configure(self, parser: CommandParser) -> None:
        """Add arguments for account_invoice_get"""
        parser.cli_argument(
            "invoice_id",
            int,
            description="""The ID of the invoice to fetch.""",
        )

    @property
    def ok_response_type(self) -> type:
        return InvoiceResponse

    def request(
        self,
        invoice_id: int,
        client: Client,
    ) -> Tuple[HTTPStatus, Union[None, InvoiceResponse, ProblemDetails]]:

        # HTTPStatus.OK: InvoiceResponse
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            invoice_id=invoice_id,
            client=client,
        )
        return page_response.status_code, page_response.parsed
