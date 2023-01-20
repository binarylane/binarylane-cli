from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Tuple, Union

from binarylane.api.server_action.server_action_power_on import sync_detailed
from binarylane.models.action_response import ActionResponse
from binarylane.models.power_on import PowerOn
from binarylane.models.power_on_type import PowerOnType
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import Mapping
from binarylane.console.runners import ActionRunner


class CommandRequest:
    server_id: int
    json_body: PowerOn

    def __init__(self, server_id: int, json_body: PowerOn) -> None:
        self.server_id = server_id
        self.json_body = json_body


class Command(ActionRunner):
    @property
    def name(self) -> str:
        return "power-on"

    @property
    def description(self) -> str:
        return """Power a Server On"""

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        mapping.add_primitive(
            "server_id",
            int,
            required=True,
            option_name=None,
            description="""The ID of the server on which the action should be performed.""",
        )

        json_body = mapping.add_json_body(PowerOn)

        json_body.add_primitive(
            "type",
            PowerOnType,
            option_name="type",
            required=True,
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
