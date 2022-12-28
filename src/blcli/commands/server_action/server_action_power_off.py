from typing import Any, Union

from ...client.api.server_action.server_action_power_off import sync_detailed
from ...client.client import Client
from ...client.models.action_response import ActionResponse
from ...client.models.power_off import PowerOff
from ...client.models.power_off_type import PowerOffType
from ...client.models.problem_details import ProblemDetails
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server-action_power-off"

    @property
    def description(self):
        return """Power a Server Off"""

    def configure(self, parser):
        """Add arguments for server-action_power-off"""
        parser.cli_argument(
            "server_id",
            description="""The target server id.""",
        )

        parser.cli_argument(
            "--type",
            dest="type",
            type=PowerOffType,
            required=True,
            description="""None""",
        )

    def request(
        self,
        server_id: int,
        client: Client,
        type: PowerOffType,
    ) -> Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]:

        return sync_detailed(
            server_id=server_id,
            client=client,
            json_body=PowerOff(
                type=type,
            ),
        ).parsed
