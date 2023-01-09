from __future__ import annotations

from typing import Any, Type, Union

from binarylane.api.server_action.server_action_change_port_blocking import sync_detailed
from binarylane.client import Client
from binarylane.models.action_response import ActionResponse
from binarylane.models.change_port_blocking import ChangePortBlocking
from binarylane.models.change_port_blocking_type import ChangePortBlockingType
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails

from binarylane.console import cli
from binarylane.console.runners import ActionRunner


class Command(ActionRunner):
    @property
    def name(self):
        return "change-port-blocking"

    @property
    def description(self):
        return """Change the Port Blocking for a Server"""

    def configure(self, parser):
        """Add arguments for server-action_change-port-blocking"""
        parser.cli_argument(
            "server_id",
            type=int,
            description="""The ID of the server on which the action should be performed.""",
        )

        parser.cli_argument(
            "--type",
            dest="type",
            type=ChangePortBlockingType,
            required=True,
            description="""None""",
        )

        parser.cli_argument(
            "--enabled",
            dest="enabled",
            type=bool,
            required=True,
            description="""The desired enabled status for port blocking.""",
            action=cli.BooleanOptionalAction,
        )

    @property
    def ok_response_type(self) -> Type:
        return ActionResponse

    def request(
        self,
        server_id: int,
        client: Client,
        type: ChangePortBlockingType,
        enabled: bool,
    ) -> Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]:

        page_response = sync_detailed(
            server_id=server_id,
            client=client,
            json_body=ChangePortBlocking(
                type=type,
                enabled=enabled,
            ),
        )
        return page_response.status_code, page_response.parsed
