from typing import Any, Type, Union

from ... import cli
from ...client.api.server_action.server_action_change_port_blocking import sync_detailed
from ...client.client import Client
from ...client.models.action_response import ActionResponse
from ...client.models.change_port_blocking import ChangePortBlocking
from ...client.models.change_port_blocking_type import ChangePortBlockingType
from ...client.models.problem_details import ProblemDetails
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...runners import ActionRunner


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
