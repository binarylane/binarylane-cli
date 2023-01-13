from __future__ import annotations

from http import HTTPStatus
from typing import Tuple, Union

from binarylane.api.domain.domain_create import sync_detailed
from binarylane.client import Client
from binarylane.models.domain_request import DomainRequest
from binarylane.models.domain_response import DomainResponse
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import UNSET, Unset

from binarylane.console.parsers import CommandParser
from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "create"

    @property
    def description(self) -> str:
        return """Create a New Domain"""

    def configure(self, parser: CommandParser) -> None:
        """Add arguments for domain_create"""

        parser.cli_argument(
            "--name",
            str,
            dest="name",
            required=True,
            description="""The domain name to add to the DNS management system.""",
        )

        parser.cli_argument(
            "--ip-address",
            Union[Unset, None, str],
            dest="ip_address",
            required=False,
            description="""An optional IPv4 address that will be used to create an A record for the root domain.""",
        )

    @property
    def ok_response_type(self) -> type:
        return DomainResponse

    def request(
        self,
        client: Client,
        name: str,
        ip_address: Union[Unset, None, str] = UNSET,
    ) -> Tuple[HTTPStatus, Union[None, DomainResponse, ValidationProblemDetails]]:

        # HTTPStatus.OK: DomainResponse
        # HTTPStatus.BAD_REQUEST: ValidationProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            client=client,
            json_body=DomainRequest(
                name=name,
                ip_address=ip_address,
            ),
        )
        return page_response.status_code, page_response.parsed
