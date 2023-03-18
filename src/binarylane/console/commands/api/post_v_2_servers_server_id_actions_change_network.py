from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Tuple, Union

from binarylane.api.server_actions.post_v_2_servers_server_id_actions_change_network import sync_detailed
from binarylane.models.action_response import ActionResponse
from binarylane.models.change_network import ChangeNetwork
from binarylane.models.change_network_type import ChangeNetworkType
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import Unset

if TYPE_CHECKING:
    from binarylane.client import Client

import binarylane.console.commands.api.get_v2_servers as api_get_v2_servers
from binarylane.console.parser import Mapping
from binarylane.console.runners.action import ActionRunner


class CommandRequest:
    server_id: int
    json_body: ChangeNetwork

    def __init__(self, server_id: int, json_body: ChangeNetwork) -> None:
        self.server_id = server_id
        self.json_body = json_body


class Command(ActionRunner):
    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/ServerActions/paths/~1v2~1servers~1%7Bserver_id%7D~1actions#ChangeNetwork/post"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        def _lookup_server_id(value: str) -> Union[None, int]:
            return api_get_v2_servers.Command(self).lookup(value)

        mapping.add_primitive(
            "server_id",
            int,
            required=True,
            option_name=None,
            description="""The ID of the server on which the action should be performed.""",
            lookup=_lookup_server_id,
        )

        json_body = mapping.add_json_body(ChangeNetwork)

        json_body.add_primitive(
            "type",
            ChangeNetworkType,
            option_name="type",
            required=True,
        )

        json_body.add_primitive(
            "vpc_id",
            Union[Unset, None, int],
            option_name="vpc-id",
            required=False,
            description="""If this is null the server will be moved into the default public network for the server's region.""",
        )

        return mapping

    @property
    def ok_response_type(self) -> type:
        return ActionResponse

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[ActionResponse, None, ProblemDetails, ValidationProblemDetails]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.OK: ActionResponse
        # HTTPStatus.ACCEPTED: Any
        # HTTPStatus.BAD_REQUEST: ValidationProblemDetails
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNPROCESSABLE_ENTITY: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            server_id=request.server_id,
            client=client,
            json_body=request.json_body,
        )
        return page_response.status_code, page_response.parsed
