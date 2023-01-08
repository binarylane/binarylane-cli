from typing import Any, Type, Union

from ... import cli
from ...client.api.server_action.server_action_change_source_and_destination_check import sync_detailed
from ...client.client import Client
from ...client.models.action_response import ActionResponse
from ...client.models.change_source_and_destination_check import ChangeSourceAndDestinationCheck
from ...client.models.change_source_and_destination_check_type import ChangeSourceAndDestinationCheckType
from ...client.models.problem_details import ProblemDetails
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...runners import ActionRunner


class Command(ActionRunner):
    @property
    def name(self):
        return "change-source-and-destination-check"

    @property
    def description(self):
        return """Enable or Disable Network Source and Destination Checks for a Server in a VPC"""

    def configure(self, parser):
        """Add arguments for server-action_change-source-and-destination-check"""
        parser.cli_argument(
            "server_id",
            type=int,
            description="""The ID of the server on which the action should be performed.""",
        )

        parser.cli_argument(
            "--type",
            dest="type",
            type=ChangeSourceAndDestinationCheckType,
            required=True,
            description="""None""",
        )

        parser.cli_argument(
            "--enabled",
            dest="enabled",
            type=bool,
            required=True,
            description="""The desired enabled status of the source and destination checks for network packets.""",
            action=cli.BooleanOptionalAction,
        )

    @property
    def ok_response_type(self) -> Type:
        return ActionResponse

    def request(
        self,
        server_id: int,
        client: Client,
        type: ChangeSourceAndDestinationCheckType,
        enabled: bool,
    ) -> Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]:

        page_response = sync_detailed(
            server_id=server_id,
            client=client,
            json_body=ChangeSourceAndDestinationCheck(
                type=type,
                enabled=enabled,
            ),
        )
        return page_response.status_code, page_response.parsed
