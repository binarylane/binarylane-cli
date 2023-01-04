from typing import Any, Union

from ...client.api.server.server_get import sync_detailed
from ...client.client import Client
from ...client.models.problem_details import ProblemDetails
from ...client.models.server_response import ServerResponse
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server_get"

    @property
    def description(self):
        return """Fetch an Existing Server"""

    def configure(self, parser):
        """Add arguments for server_get"""
        parser.cli_argument(
            "server_id",
            type=int,
            description="""The target server id.""",
        )

    def request(
        self,
        server_id: int,
        client: Client,
    ) -> Union[Any, ProblemDetails, ServerResponse]:

        return sync_detailed(
            server_id=server_id,
            client=client,
        ).parsed
