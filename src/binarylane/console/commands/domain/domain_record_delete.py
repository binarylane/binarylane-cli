from __future__ import annotations

from http import HTTPStatus
from typing import Tuple, Union

from binarylane.api.domain.domain_record_delete import sync_detailed
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
        return """Delete an Existing Domain Record"""

    def configure(self, parser: CommandParser) -> None:
        """Add arguments for domain_record_delete"""
        parser.cli_argument(
            "domain_name",
            str,
            description="""The domain name for which the record should be deleted.""",
        )
        parser.cli_argument(
            "record_id",
            int,
            description="""The ID of the record to delete.""",
        )

    @property
    def ok_response_type(self) -> type:
        return type(None)

    def request(
        self,
        domain_name: str,
        record_id: int,
        client: Client,
    ) -> Tuple[HTTPStatus, Union[None, ProblemDetails]]:

        # HTTPStatus.NO_CONTENT: Any
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            domain_name=domain_name,
            record_id=record_id,
            client=client,
        )
        return page_response.status_code, page_response.parsed
