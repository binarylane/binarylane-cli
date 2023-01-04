from typing import Any, Union

from ... import cli
from ...client.api.action.action_proceed import sync_detailed
from ...client.client import Client
from ...client.models.problem_details import ProblemDetails
from ...client.models.proceed_request import ProceedRequest
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "action_proceed"

    @property
    def description(self):
        return """Respond to a UserInteractionRequired Action"""

    def configure(self, parser):
        """Add arguments for action_proceed"""
        parser.cli_argument(
            "action_id",
            type=int,
        )

        parser.cli_argument(
            "--proceed",
            dest="proceed",
            type=bool,
            required=True,
            description="""Please see the documentation for each type of interaction for the effect of providing 'true' or 'false' here.""",
            action=cli.BooleanOptionalAction,
        )

    def request(
        self,
        action_id: int,
        client: Client,
        proceed: bool,
    ) -> Union[Any, ProblemDetails]:

        return sync_detailed(
            action_id=action_id,
            client=client,
            json_body=ProceedRequest(
                proceed=proceed,
            ),
        ).parsed
