from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Tuple, Union

from binarylane.api.server_actions.post_v_2_servers_server_id_actions_resize_disk import sync_detailed
from binarylane.models.action_response import ActionResponse
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.resize_disk import ResizeDisk
from binarylane.models.resize_disk_type import ResizeDiskType
from binarylane.models.validation_problem_details import ValidationProblemDetails

if TYPE_CHECKING:
    from binarylane.client import Client

import binarylane.console.commands.api.get_v2_servers as api_get_v2_servers
from binarylane.console.parser import Mapping, PrimitiveAttribute
from binarylane.console.runners.action import ActionRunner


class CommandRequest:
    server_id: int
    json_body: ResizeDisk

    def __init__(self, server_id: int, json_body: ResizeDisk) -> None:
        self.server_id = server_id
        self.json_body = json_body


class Command(ActionRunner):
    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/ServerActions/paths/~1v2~1servers~1%7Bserver_id%7D~1actions#ResizeDisk/post"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        def _lookup_server_id(value: str) -> Union[None, int]:
            return api_get_v2_servers.Command(self._context).lookup(value)

        mapping.add(
            PrimitiveAttribute(
                "server_id",
                int,
                required=True,
                option_name=None,
                description="""The ID of the server on which the action should be performed.""",
                lookup=_lookup_server_id,
            )
        )

        json_body = mapping.add_json_body(ResizeDisk)

        json_body.add(
            PrimitiveAttribute(
                "type",
                ResizeDiskType,
                required=True,
                option_name="type",
            )
        )

        json_body.add(
            PrimitiveAttribute(
                "disk_id",
                int,
                required=True,
                option_name="disk-id",
                description="""The ID of the existing disk. See server.disks for a list of IDs.""",
            )
        )

        json_body.add(
            PrimitiveAttribute(
                "size_gigabytes",
                int,
                required=True,
                option_name="size-gigabytes",
                description="""The new size of the disk in GB. If increasing the size of the disk the server must have sufficient unallocated storage space.""",
            )
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
