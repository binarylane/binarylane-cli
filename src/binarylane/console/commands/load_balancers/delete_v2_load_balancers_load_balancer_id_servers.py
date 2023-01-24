from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, List, Tuple, Union

from binarylane.api.load_balancers.delete_v2_load_balancers_load_balancer_id_servers import sync_detailed
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.server_ids_request import ServerIdsRequest
from binarylane.models.validation_problem_details import ValidationProblemDetails

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import Mapping
from binarylane.console.runners.command import CommandRunner


class CommandRequest:
    load_balancer_id: int
    json_body: ServerIdsRequest

    def __init__(self, load_balancer_id: int, json_body: ServerIdsRequest) -> None:
        self.load_balancer_id = load_balancer_id
        self.json_body = json_body


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "delete"

    @property
    def description(self) -> str:
        return """Remove Servers from an Existing Load Balancer"""

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        mapping.add_primitive(
            "load_balancer_id",
            int,
            required=True,
            option_name=None,
            description="""The ID of the load balancer for which servers should be removed.""",
        )

        json_body = mapping.add_json_body(ServerIdsRequest)

        json_body.add_primitive(
            "server_ids",
            List[int],
            option_name="server-ids",
            required=True,
            description="""A list of server IDs.""",
        )

        return mapping

    @property
    def ok_response_type(self) -> type:
        return type(None)

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[None, ProblemDetails, ValidationProblemDetails]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.NO_CONTENT: Any
        # HTTPStatus.BAD_REQUEST: ValidationProblemDetails
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNPROCESSABLE_ENTITY: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            load_balancer_id=request.load_balancer_id,
            client=client,
            json_body=request.json_body,
        )
        return page_response.status_code, page_response.parsed