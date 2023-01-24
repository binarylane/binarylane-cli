from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Tuple, Union

from binarylane.api.server_actions.post_v_2_servers_server_id_actions_change_separate_private_network_interface import (
    sync_detailed,
)
from binarylane.models.action_response import ActionResponse
from binarylane.models.change_separate_private_network_interface import ChangeSeparatePrivateNetworkInterface
from binarylane.models.change_separate_private_network_interface_type import ChangeSeparatePrivateNetworkInterfaceType
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import Mapping
from binarylane.console.runners.action import ActionRunner


class CommandRequest:
    server_id: int
    json_body: ChangeSeparatePrivateNetworkInterface

    def __init__(self, server_id: int, json_body: ChangeSeparatePrivateNetworkInterface) -> None:
        self.server_id = server_id
        self.json_body = json_body


class Command(ActionRunner):
    @property
    def name(self) -> str:
        return "change-separate-private-network-interface"

    @property
    def description(self) -> str:
        return """Enable or Disable a Separate Private Network Interface for a Server in a VPC"""

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        mapping.add_primitive(
            "server_id",
            int,
            required=True,
            option_name=None,
            description="""The ID of the server on which the action should be performed.""",
        )

        json_body = mapping.add_json_body(ChangeSeparatePrivateNetworkInterface)

        json_body.add_primitive(
            "type",
            ChangeSeparatePrivateNetworkInterfaceType,
            option_name="type",
            required=True,
        )

        json_body.add_primitive(
            "enabled",
            bool,
            option_name="enabled",
            required=True,
            description="""The desired enabled status of the separate second network interface.""",
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