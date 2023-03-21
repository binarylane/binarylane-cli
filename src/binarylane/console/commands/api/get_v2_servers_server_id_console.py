from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Tuple, Union

from binarylane.api.servers.get_v2_servers_server_id_console import sync_detailed
from binarylane.models.console_response import ConsoleResponse
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import Mapping, PrimitiveAttribute
from binarylane.console.runners.command import CommandRunner


class CommandRequest:
    server_id: int

    def __init__(self, server_id: int) -> None:
        self.server_id = server_id


class Command(CommandRunner):
    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/Servers/paths/~1v2~1servers~1%7Bserver_id%7D~1console/get"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        mapping.add(
            PrimitiveAttribute(
                "server_id",
                int,
                required=True,
                option_name=None,
                description="""The ID of the server for which console URLs will be fetched.""",
            )
        )

        return mapping

    @property
    def ok_response_type(self) -> type:
        return ConsoleResponse

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[None, ConsoleResponse, ProblemDetails, ValidationProblemDetails]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.OK: ConsoleResponse
        # HTTPStatus.BAD_REQUEST: ValidationProblemDetails
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            server_id=request.server_id,
            client=client,
        )
        return page_response.status_code, page_response.parsed
