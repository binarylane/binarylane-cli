from __future__ import annotations

from http import HTTPStatus
from typing import Tuple, Union

from binarylane.api.action.action_get import sync_detailed
from binarylane.client import Client
from binarylane.models.action_response import ActionResponse
from binarylane.models.problem_details import ProblemDetails

from binarylane.console.parsers import CommandParser
from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "get"

    @property
    def description(self) -> str:
        return """Fetch an Existing Action"""

    def configure(self, parser: CommandParser) -> None:
        """Add arguments for action_get"""
        parser.cli_argument(
            "action_id",
            int,
            description="""The ID of the action to fetch.""",
        )

    @property
    def ok_response_type(self) -> type:
        return ActionResponse

    def request(
        self,
        action_id: int,
        client: Client,
    ) -> Tuple[HTTPStatus, Union[ActionResponse, None, ProblemDetails]]:

        # HTTPStatus.OK: ActionResponse
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            action_id=action_id,
            client=client,
        )
        return page_response.status_code, page_response.parsed
