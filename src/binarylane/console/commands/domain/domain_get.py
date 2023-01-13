from __future__ import annotations

from http import HTTPStatus
from typing import Tuple, Union

from binarylane.api.domain.domain_get import sync_detailed
from binarylane.client import Client
from binarylane.models.domain_response import DomainResponse
from binarylane.models.problem_details import ProblemDetails

from binarylane.console.parsers import CommandParser
from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "get"

    @property
    def description(self) -> str:
        return """Fetch an Existing Domain"""

    def configure(self, parser: CommandParser) -> None:
        """Add arguments for domain_get"""
        parser.cli_argument(
            "domain_name",
            str,
            description="""The name of the domain to fetch.""",
        )

    @property
    def ok_response_type(self) -> type:
        return DomainResponse

    def request(
        self,
        domain_name: str,
        client: Client,
    ) -> Tuple[HTTPStatus, Union[None, DomainResponse, ProblemDetails]]:

        # HTTPStatus.OK: DomainResponse
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            domain_name=domain_name,
            client=client,
        )
        return page_response.status_code, page_response.parsed
