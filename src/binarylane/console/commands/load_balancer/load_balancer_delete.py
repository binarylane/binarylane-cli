from __future__ import annotations

from http import HTTPStatus
from typing import Tuple, Union

from binarylane.api.load_balancer.load_balancer_delete import sync_detailed
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
        return """Cancel an Existing Load Balancer"""

    def configure(self, parser: CommandParser) -> None:
        """Add arguments for load-balancer_delete"""
        parser.cli_argument(
            "load_balancer_id",
            int,
            description="""The ID of the load balancer to cancel.""",
        )

    @property
    def ok_response_type(self) -> type:
        return type(None)

    def request(
        self,
        load_balancer_id: int,
        client: Client,
    ) -> Tuple[HTTPStatus, Union[None, ProblemDetails]]:

        # HTTPStatus.NO_CONTENT: Any
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            load_balancer_id=load_balancer_id,
            client=client,
        )
        return page_response.status_code, page_response.parsed
