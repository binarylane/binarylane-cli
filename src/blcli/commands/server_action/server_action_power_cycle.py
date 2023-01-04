from typing import Any, Union

from ...client.api.server_action.server_action_power_cycle import sync_detailed
from ...client.client import Client
from ...client.models.action_response import ActionResponse
from ...client.models.power_cycle import PowerCycle
from ...client.models.power_cycle_type import PowerCycleType
from ...client.models.problem_details import ProblemDetails
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "power-cycle"

    @property
    def description(self):
        return """Power a Server Off and then On"""

    def configure(self, parser):
        """Add arguments for server-action_power-cycle"""
        parser.cli_argument(
            "server_id",
            type=int,
            description="""The target server id.""",
        )

        parser.cli_argument(
            "--type",
            dest="type",
            type=PowerCycleType,
            required=True,
            description="""None""",
        )

    def request(
        self,
        server_id: int,
        client: Client,
        type: PowerCycleType,
    ) -> Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]:

        return sync_detailed(
            server_id=server_id,
            client=client,
            json_body=PowerCycle(
                type=type,
            ),
        ).parsed
