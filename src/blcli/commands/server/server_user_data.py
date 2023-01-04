from typing import Any, Union

from ...client.api.server.server_user_data import sync_detailed
from ...client.client import Client
from ...client.models.problem_details import ProblemDetails
from ...client.models.user_data import UserData
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server_user-data"

    @property
    def description(self):
        return """Fetch the Currently Set UserData for a Server"""

    def configure(self, parser):
        """Add arguments for server_user-data"""
        parser.cli_argument(
            "server_id",
            type=int,
            description="""The target server id.""",
        )

    def request(
        self,
        server_id: int,
        client: Client,
    ) -> Union[Any, ProblemDetails, UserData]:

        return sync_detailed(
            server_id=server_id,
            client=client,
        ).parsed
