from typing import Any, Union

from ...client.api.server_action.server_action_uptime import sync_detailed
from ...client.client import Client
from ...client.models.action_response import ActionResponse
from ...client.models.problem_details import ProblemDetails
from ...client.models.uptime import Uptime
from ...client.models.uptime_type import UptimeType
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server-action_uptime"

    @property
    def description(self):
        return """Check the Uptime of a Server"""

    def configure(self, parser):
        """Add arguments for server-action_uptime"""
        parser.cli_argument(
            "server_id",
            description="""The target server id.""",
        )

        parser.cli_argument(
            "--type",
            dest="type",
            type=UptimeType,
            required=True,
            description="""None""",
        )

    def request(
        self,
        server_id: int,
        client: Client,
        type: UptimeType,
    ) -> Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]:

        return sync_detailed(
            server_id=server_id,
            client=client,
            json_body=Uptime(
                type=type,
            ),
        ).parsed
