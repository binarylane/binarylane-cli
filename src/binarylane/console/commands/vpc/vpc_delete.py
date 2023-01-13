from __future__ import annotations

from http import HTTPStatus
from typing import Tuple, Union

from binarylane.api.vpc.vpc_delete import sync_detailed
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
        return """Delete an Existing VPC"""

    def configure(self, parser: CommandParser) -> None:
        """Add arguments for vpc_delete"""
        parser.cli_argument(
            "vpc_id",
            int,
            description="""The target vpc id.""",
        )

    @property
    def ok_response_type(self) -> type:
        return type(None)

    def request(
        self,
        vpc_id: int,
        client: Client,
    ) -> Tuple[HTTPStatus, Union[None, ProblemDetails]]:

        # HTTPStatus.NO_CONTENT: Any
        # HTTPStatus.FORBIDDEN: ProblemDetails
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            vpc_id=vpc_id,
            client=client,
        )
        return page_response.status_code, page_response.parsed
