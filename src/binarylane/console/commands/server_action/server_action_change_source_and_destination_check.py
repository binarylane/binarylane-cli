from __future__ import annotations

from http import HTTPStatus
from typing import Tuple, Union

from binarylane.api.server_action.server_action_change_source_and_destination_check import sync_detailed
from binarylane.client import Client
from binarylane.models.action_response import ActionResponse
from binarylane.models.change_source_and_destination_check import ChangeSourceAndDestinationCheck
from binarylane.models.change_source_and_destination_check_type import ChangeSourceAndDestinationCheckType
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails

from binarylane.console.actions import BooleanOptionalAction
from binarylane.console.parsers import CommandParser
from binarylane.console.runners import ActionRunner


class Command(ActionRunner):
    @property
    def name(self) -> str:
        return "change-source-and-destination-check"

    @property
    def description(self) -> str:
        return """Enable or Disable Network Source and Destination Checks for a Server in a VPC"""

    def configure(self, parser: CommandParser) -> None:
        """Add arguments for server-action_change-source-and-destination-check"""
        parser.cli_argument(
            "server_id",
            int,
            description="""The ID of the server on which the action should be performed.""",
        )

        parser.cli_argument(
            "--type",
            ChangeSourceAndDestinationCheckType,
            dest="type",
            required=True,
            description="""None""",
        )

        parser.cli_argument(
            "--enabled",
            bool,
            dest="enabled",
            required=True,
            description="""The desired enabled status of the source and destination checks for network packets.""",
            action=BooleanOptionalAction,
        )

    @property
    def ok_response_type(self) -> type:
        return ActionResponse

    def request(
        self,
        server_id: int,
        client: Client,
        type: ChangeSourceAndDestinationCheckType,
        enabled: bool,
    ) -> Tuple[HTTPStatus, Union[ActionResponse, None, ProblemDetails, ValidationProblemDetails]]:

        # HTTPStatus.OK: ActionResponse
        # HTTPStatus.ACCEPTED: Any
        # HTTPStatus.BAD_REQUEST: ValidationProblemDetails
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNPROCESSABLE_ENTITY: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            server_id=server_id,
            client=client,
            json_body=ChangeSourceAndDestinationCheck(
                type=type,
                enabled=enabled,
            ),
        )
        return page_response.status_code, page_response.parsed
