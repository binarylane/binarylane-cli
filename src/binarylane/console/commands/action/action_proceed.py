from __future__ import annotations

from http import HTTPStatus
from typing import Tuple, Union

from binarylane.api.action.action_proceed import sync_detailed
from binarylane.client import Client
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.proceed_request import ProceedRequest

from binarylane.console.actions import BooleanOptionalAction
from binarylane.console.parsers import CommandParser
from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "proceed"

    @property
    def description(self) -> str:
        return """Respond to a UserInteractionRequired Action"""

    def configure(self, parser: CommandParser) -> None:
        """Add arguments for action_proceed"""
        parser.cli_argument(
            "action_id",
            int,
            description="""The ID of the action for which this is a response.""",
        )

        parser.cli_argument(
            "--proceed",
            bool,
            dest="proceed",
            required=True,
            description="""Please see the documentation for each type of interaction for the effect of providing 'true' or 'false' here.""",
            action=BooleanOptionalAction,
        )

    @property
    def ok_response_type(self) -> type:
        return type(None)

    def request(
        self,
        action_id: int,
        client: Client,
        proceed: bool,
    ) -> Tuple[HTTPStatus, Union[None, ProblemDetails]]:

        # HTTPStatus.NO_CONTENT: Any
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            action_id=action_id,
            client=client,
            json_body=ProceedRequest(
                proceed=proceed,
            ),
        )
        return page_response.status_code, page_response.parsed
