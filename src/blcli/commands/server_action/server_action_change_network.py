from typing import Any, Type, Union

from ...client.api.server_action.server_action_change_network import sync_detailed
from ...client.client import Client
from ...client.models.action_response import ActionResponse
from ...client.models.change_network import ChangeNetwork
from ...client.models.change_network_type import ChangeNetworkType
from ...client.models.problem_details import ProblemDetails
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...client.types import UNSET, Unset
from ...runners import ActionRunner


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
