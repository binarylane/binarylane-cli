from typing import Any, List, Type, Union

from ...client.api.server.server_failover_ip_update import sync_detailed
from ...client.client import Client
from ...client.models.action_response import ActionResponse
from ...client.models.problem_details import ProblemDetails
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...runners import ActionRunner


class Command(ActionRunner):
    @property
    def name(self):
        return "update"

    @property
    def description(self):
        return """Sets the List of Failover IPs that are Assigned to a Server"""

    def configure(self, parser):
        """Add arguments for server_failover-ip_update"""
        parser.cli_argument(
            "server_id",
            type=int,
            description="""The target server id.""",
        )

        parser.cli_argument(
            "--value",
            nargs="*",
        )

    @property
    def ok_response_type(self) -> Type:
        return ActionResponse

    def request(
        self, server_id: int, client: Client, server: List[str]
    ) -> Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]:

        page_response = sync_detailed(
            server_id=server_id,
            client=client,
            json_body=server,
        )
        return page_response.status_code, page_response.parsed
