from typing import Any, Union

from ...client.api.server_action.server_action_shutdown import sync_detailed
from ...client.client import Client
from ...client.models.action_response import ActionResponse
from ...client.models.problem_details import ProblemDetails
from ...client.models.shutdown import Shutdown
from ...client.models.shutdown_type import ShutdownType
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server-action_shutdown"

    @property
    def description(self):
        return """Request a Server Perform a Shutdown"""

    def configure(self, parser):
        """Add arguments for server-action_shutdown"""
        parser.cli_argument(
            "server_id",
            description="""The target server id.""",
        )

        parser.cli_argument(
            "--type",
            dest="type",
            type=ShutdownType,
            required=True,
            description="""None""",
        )

    def request(
        self,
        server_id: int,
        client: Client,
        type: ShutdownType,
    ) -> Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]:

        return sync_detailed(
            server_id=server_id,
            client=client,
            json_body=Shutdown(
                type=type,
            ),
        ).parsed
