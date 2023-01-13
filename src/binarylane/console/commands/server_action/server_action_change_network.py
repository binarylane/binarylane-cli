from __future__ import annotations

from http import HTTPStatus
from typing import Tuple, Union

from binarylane.api.server_action.server_action_change_network import sync_detailed
from binarylane.client import Client
from binarylane.models.action_response import ActionResponse
from binarylane.models.change_network import ChangeNetwork
from binarylane.models.change_network_type import ChangeNetworkType
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import UNSET, Unset

from binarylane.console.parsers import CommandParser
from binarylane.console.runners import ActionRunner


class Command(ActionRunner):
    @property
    def name(self) -> str:
        return "change-network"

    @property
    def description(self) -> str:
        return """Move a Server to an Existing Network"""

    def configure(self, parser: CommandParser) -> None:
        """Add arguments for server-action_change-network"""
        parser.cli_argument(
            "server_id",
            int,
            description="""The ID of the server on which the action should be performed.""",
        )

        parser.cli_argument(
            "--type",
            ChangeNetworkType,
            dest="type",
            required=True,
            description="""None""",
        )

        parser.cli_argument(
            "--vpc-id",
            Union[Unset, None, int],
            dest="vpc_id",
            required=False,
            description="""If this is null the server will be moved into the default public network for the server's region.""",
        )

    @property
    def ok_response_type(self) -> type:
        return ActionResponse

    def request(
        self,
        server_id: int,
        client: Client,
        type: ChangeNetworkType,
        vpc_id: Union[Unset, None, int] = UNSET,
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
            json_body=ChangeNetwork(
                type=type,
                vpc_id=vpc_id,
            ),
        )
        return page_response.status_code, page_response.parsed
