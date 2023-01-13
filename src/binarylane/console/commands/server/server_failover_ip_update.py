from __future__ import annotations

from http import HTTPStatus
from typing import List, Tuple, Union

from binarylane.api.server.server_failover_ip_update import sync_detailed
from binarylane.client import Client
from binarylane.models.action_response import ActionResponse
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails

from binarylane.console.parsers import CommandParser
from binarylane.console.runners import ActionRunner


class Command(ActionRunner):
    @property
    def name(self) -> str:
        return "update"

    @property
    def description(self) -> str:
        return """Sets the List of Failover IPs that are Assigned to a Server"""

    def configure(self, parser: CommandParser) -> None:
        """Add arguments for server_failover-ip_update"""
        parser.cli_argument(
            "server_id",
            int,
            description="""The target server id.""",
        )

        parser.cli_argument(
            "--value",
            List[str],
            warning="request body is List[str]",
        )

    @property
    def ok_response_type(self) -> type:
        return ActionResponse

    def request(
        self, server_id: int, client: Client, server: List[str]
    ) -> Tuple[HTTPStatus, Union[ActionResponse, None, ProblemDetails, ValidationProblemDetails]]:

        # HTTPStatus.OK: ActionResponse
        # HTTPStatus.NO_CONTENT: Any
        # HTTPStatus.BAD_REQUEST: ValidationProblemDetails
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            server_id=server_id,
            client=client,
            json_body=server,
        )
        return page_response.status_code, page_response.parsed
