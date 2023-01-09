from __future__ import annotations

from typing import Any, Type, Union

from binarylane.api.server_action.server_action_change_network import sync_detailed
from binarylane.client import Client
from binarylane.models.action_response import ActionResponse
from binarylane.models.change_network import ChangeNetwork
from binarylane.models.change_network_type import ChangeNetworkType
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import UNSET, Unset

from binarylane.console.runners import ActionRunner


class Command(ActionRunner):
    @property
    def name(self):
        return "change-network"

    @property
    def description(self):
        return """Move a Server to an Existing Network"""

    def configure(self, parser):
        """Add arguments for server-action_change-network"""
        parser.cli_argument(
            "server_id",
            type=int,
            description="""The ID of the server on which the action should be performed.""",
        )

        parser.cli_argument(
            "--type",
            dest="type",
            type=ChangeNetworkType,
            required=True,
            description="""None""",
        )

        parser.cli_argument(
            "--vpc-id",
            dest="vpc_id",
            type=Union[Unset, None, int],
            required=False,
            description="""If this is null the server will be moved into the default public network for the server's region.""",
        )

    @property
    def ok_response_type(self) -> Type:
        return ActionResponse

    def request(
        self,
        server_id: int,
        client: Client,
        type: ChangeNetworkType,
        vpc_id: Union[Unset, None, int] = UNSET,
    ) -> Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]:

        page_response = sync_detailed(
            server_id=server_id,
            client=client,
            json_body=ChangeNetwork(
                type=type,
                vpc_id=vpc_id,
            ),
        )
        return page_response.status_code, page_response.parsed
