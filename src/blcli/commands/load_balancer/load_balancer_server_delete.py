from typing import Any, List, Type, Union

from ...client.api.load_balancer.load_balancer_server_delete import sync_detailed
from ...client.client import Client
from ...client.models.problem_details import ProblemDetails
from ...client.models.server_ids_request import ServerIdsRequest
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "delete"

    @property
    def description(self):
        return """Remove Servers from an Existing Load Balancer"""

    def configure(self, parser):
        """Add arguments for load-balancer_server_delete"""
        parser.cli_argument(
            "load_balancer_id",
            type=int,
            description="""The ID of the load balancer for which servers should be removed.""",
        )

        parser.cli_argument(
            "--server-ids",
            dest="server_ids",
            type=List[int],
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
