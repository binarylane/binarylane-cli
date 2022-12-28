from typing import Any, Union

from ...client.api.server_action.server_action_power_on import sync_detailed
from ...client.client import Client
from ...client.models.action_response import ActionResponse
from ...client.models.power_on import PowerOn
from ...client.models.power_on_type import PowerOnType
from ...client.models.problem_details import ProblemDetails
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server-action_power-on"

    @property
    def description(self):
        return """Power a Server On"""

    def configure(self, parser):
        """Add arguments for server-action_power-on"""
        parser.cli_argument(
            "server_id",
            description="""The target server id.""",
        )

        parser.cli_argument(
            "--type",
            dest="type",
            type=PowerOnType,
            required=True,
            description="""None""",
        )

    def request(
        self,
        server_id: int,
        client: Client,
        type: PowerOnType,
    ) -> Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]:

        return sync_detailed(
            server_id=server_id,
            client=client,
            json_body=PowerOn(
                type=type,
            ),
        ).parsed
