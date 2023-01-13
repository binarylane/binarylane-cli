from __future__ import annotations

from http import HTTPStatus
from typing import List, Tuple, Union

from binarylane.api.load_balancer.load_balancer_server_create import sync_detailed
from binarylane.client import Client
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.server_ids_request import ServerIdsRequest
from binarylane.models.validation_problem_details import ValidationProblemDetails

from binarylane.console.parsers import CommandParser
from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "create"

    @property
    def description(self) -> str:
        return """Add Servers to an Existing Load Balancer"""

    def configure(self, parser: CommandParser) -> None:
        """Add arguments for load-balancer_server_create"""
        parser.cli_argument(
            "load_balancer_id",
            int,
            description="""The ID of the load balancer to which servers should be added.""",
        )

        parser.cli_argument(
            "--server-ids",
            List[int],
            dest="server_ids",
            required=True,
            description="""A list of server IDs.""",
        )

    @property
    def ok_response_type(self) -> type:
        return type(None)

    def request(
        self,
        load_balancer_id: int,
        client: Client,
        server_ids: List[int],
    ) -> Tuple[HTTPStatus, Union[None, ProblemDetails, ValidationProblemDetails]]:

        # HTTPStatus.NO_CONTENT: Any
        # HTTPStatus.BAD_REQUEST: ValidationProblemDetails
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNPROCESSABLE_ENTITY: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            load_balancer_id=load_balancer_id,
            client=client,
            json_body=ServerIdsRequest(
                server_ids=server_ids,
            ),
        )
        return page_response.status_code, page_response.parsed
