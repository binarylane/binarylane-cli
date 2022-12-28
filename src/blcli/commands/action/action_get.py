from typing import Any, Union

from ...client.api.action.action_get import sync_detailed
from ...client.client import Client
from ...client.models.action_response import ActionResponse
from ...client.models.problem_details import ProblemDetails
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "action_get"

    @property
    def description(self):
        return """Fetch an Existing Action"""

    def configure(self, parser):
        """Add arguments for action_get"""
        parser.cli_argument(
            "action_id",
        )

    def request(
        self,
        action_id: int,
        client: Client,
    ) -> Union[ActionResponse, Any, ProblemDetails]:

        return sync_detailed(
            action_id=action_id,
            client=client,
        ).parsed
