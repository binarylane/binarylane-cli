from typing import Any, Union

from ...client.api.server.server_action_get import sync_detailed
from ...client.client import Client
from ...client.models.action_response import ActionResponse
from ...client.models.problem_details import ProblemDetails
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "get"

    @property
    def description(self):
        return """Fetch an Action for a Server"""

    def configure(self, parser):
        """Add arguments for server_action_get"""
        parser.cli_argument(
            "server_id",
            type=int,
            description="""The target server id.""",
        )
        parser.cli_argument(
            "action_id",
            type=int,
        )

    def request(
        self,
        server_id: int,
        action_id: int,
        client: Client,
    ) -> Union[ActionResponse, Any, ProblemDetails]:

        return sync_detailed(
            server_id=server_id,
            action_id=action_id,
            client=client,
        ).parsed
