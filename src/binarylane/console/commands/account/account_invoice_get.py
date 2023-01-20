from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Tuple, Union

from binarylane.api.account.account_invoice_get import sync_detailed
from binarylane.models.invoice_response import InvoiceResponse
from binarylane.models.problem_details import ProblemDetails

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import Mapping
from binarylane.console.runners.command import CommandRunner


class CommandRequest:
    invoice_id: int

    def __init__(self, invoice_id: int) -> None:
        self.invoice_id = invoice_id


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "get"

    @property
    def description(self) -> str:
        return """Fetch an Invoice"""

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        mapping.add_primitive(
            "invoice_id",
            int,
            required=True,
            option_name=None,
            description="""The ID of the invoice to fetch.""",
        )

        return mapping

    @property
    def ok_response_type(self) -> type:
        return InvoiceResponse

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[None, InvoiceResponse, ProblemDetails]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.OK: InvoiceResponse
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            invoice_id=request.invoice_id,
            client=client,
        )
        return page_response.status_code, page_response.parsed
