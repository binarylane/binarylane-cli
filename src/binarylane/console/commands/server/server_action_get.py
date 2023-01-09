from __future__ import annotations

from typing import Any, Type, Union

from binarylane.api.server.server_action_get import sync_detailed
from binarylane.client import Client
from binarylane.models.action_response import ActionResponse
from binarylane.models.problem_details import ProblemDetails

from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "get"

    @property
    def description(self):
        return """Fetch an Action for a Server"""

    def configure(self, parser):
        """Add arguments for server_action_get"""
        parser.cli_argument(
            "server_id",
            type=int,
            description="""The ID of the server for which the action should be fetched.""",
        )
        parser.cli_argument(
            "action_id",
            type=int,
            description="""The ID of the action to fetch.""",
        )

    @property
    def ok_response_type(self) -> Type:
        return ActionResponse

    def request(
        self,
        server_id: int,
        action_id: int,
        client: Client,
    ) -> Union[ActionResponse, Any, ProblemDetails]:

        page_response = sync_detailed(
            server_id=server_id,
            action_id=action_id,
            client=client,
        )
        return page_response.status_code, page_response.parsed