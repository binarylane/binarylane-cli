from __future__ import annotations

from typing import Any, List, Type, Union

from binarylane.api.load_balancer.load_balancer_server_create import sync_detailed
from binarylane.client import Client
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.server_ids_request import ServerIdsRequest
from binarylane.models.validation_problem_details import ValidationProblemDetails

from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "create"

    @property
    def description(self):
        return """Add Servers to an Existing Load Balancer"""

    def configure(self, parser):
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
    def ok_response_type(self) -> Type:
        return type(None)

    def request(
        self,
        load_balancer_id: int,
        client: Client,
        server_ids: List[int],
    ) -> Union[Any, ProblemDetails, ValidationProblemDetails]:

        page_response = sync_detailed(
            load_balancer_id=load_balancer_id,
            client=client,
            json_body=ServerIdsRequest(
                server_ids=server_ids,
            ),
        )
        return page_response.status_code, page_response.parsed
