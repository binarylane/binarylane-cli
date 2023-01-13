from __future__ import annotations

from http import HTTPStatus
from typing import Tuple, Union

from binarylane.api.domain.domain_delete import sync_detailed
from binarylane.client import Client
from binarylane.models.problem_details import ProblemDetails

from binarylane.console.parsers import CommandParser
from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "delete"

    @property
    def description(self) -> str:
        return """Delete an Existing Domain"""

    def configure(self, parser: CommandParser) -> None:
        """Add arguments for domain_delete"""
        parser.cli_argument(
            "domain_name",
            str,
            description="""The name of the domain to delete.""",
        )

    @property
    def ok_response_type(self) -> type:
        return type(None)

    def request(
        self,
        domain_name: str,
        client: Client,
    ) -> Tuple[HTTPStatus, Union[None, ProblemDetails]]:

        # HTTPStatus.NO_CONTENT: Any
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            domain_name=domain_name,
            client=client,
        )
        return page_response.status_code, page_response.parsed
