from typing import Any, Union

from ...client.api.server_action.server_action_is_running import sync_detailed
from ...client.client import Client
from ...client.models.action_response import ActionResponse
from ...client.models.is_running import IsRunning
from ...client.models.is_running_type import IsRunningType
from ...client.models.problem_details import ProblemDetails
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server-action_is-running"

    @property
    def description(self):
        return """Check if a Server is Running"""

    def configure(self, parser):
        """Add arguments for server-action_is-running"""
        parser.cli_argument(
            "server_id",
            description="""The target server id.""",
        )

        parser.cli_argument(
            "--type",
            dest="type",
            type=IsRunningType,
            required=True,
            description="""None""",
        )

    def request(
        self,
        server_id: int,
        client: Client,
        type: IsRunningType,
    ) -> Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]:

        return sync_detailed(
            server_id=server_id,
            client=client,
            json_body=IsRunning(
                type=type,
            ),
        ).parsed
