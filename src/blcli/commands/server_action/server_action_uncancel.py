from typing import Any, Union

from ...client.api.server_action.server_action_uncancel import sync_detailed
from ...client.client import Client
from ...client.models.action_response import ActionResponse
from ...client.models.problem_details import ProblemDetails
from ...client.models.uncancel import Uncancel
from ...client.models.uncancel_type import UncancelType
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server-action_uncancel"

    @property
    def description(self):
        return """Revert the Cancellation of a Server"""

    def configure(self, parser):
        """Add arguments for server-action_uncancel"""
        parser.cli_argument(
            "server_id",
            description="""The target server id.""",
        )

        parser.cli_argument(
            "--type",
            dest="type",
            type=UncancelType,
            required=True,
            description="""None""",
        )

    def request(
        self,
        server_id: int,
        client: Client,
        type: UncancelType,
    ) -> Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]:

        return sync_detailed(
            server_id=server_id,
            client=client,
            json_body=Uncancel(
                type=type,
            ),
        ).parsed
