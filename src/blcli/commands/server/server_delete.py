from typing import Any, Union

from ...client.api.server.server_delete import sync_detailed
from ...client.client import Client
from ...client.models.problem_details import ProblemDetails
from ...client.types import UNSET, Unset
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "delete"

    @property
    def description(self):
        return """Cancel an Existing Server"""

    def configure(self, parser):
        """Add arguments for server_delete"""
        parser.cli_argument(
            "server_id",
            type=int,
            description="""The ID of the server to be cancelled.""",
        )

        parser.cli_argument(
            "--reason",
            dest="reason",
            type=Union[Unset, None, str],
            required=False,
            description="""None""",
        )

    def request(
        self,
        server_id: int,
        client: Client,
        reason: Union[Unset, None, str] = UNSET,
    ) -> Union[Any, ProblemDetails]:

        return sync_detailed(
            server_id=server_id,
            client=client,
            reason=reason,
        ).parsed
