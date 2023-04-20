from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Tuple, Union

from binarylane.api.server_actions.post_v_2_servers_server_id_actions_add_disk import sync_detailed
from binarylane.models.action_response import ActionResponse
from binarylane.models.add_disk import AddDisk
from binarylane.models.add_disk_type import AddDiskType
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import Unset

if TYPE_CHECKING:
    from binarylane.client import Client

import binarylane.console.commands.api.get_v2_servers as api_get_v2_servers
from binarylane.console.parser import Mapping, PrimitiveAttribute
from binarylane.console.runners.action import ActionRunner


class CommandRequest:
    server_id: int
    json_body: AddDisk

    def __init__(self, server_id: int, json_body: AddDisk) -> None:
        self.server_id = server_id
        self.json_body = json_body


class Command(ActionRunner):
    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/ServerActions/paths/~1v2~1servers~1%7Bserver_id%7D~1actions#AddDisk/post"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        def lookup_server_id(ref: str) -> Union[None, int]:
            return api_get_v2_servers.Command(self._context).lookup(ref)

        mapping.add(
            PrimitiveAttribute(
                "server_id",
                int,
                required=True,
                option_name=None,
                metavar="server",
                description="""The ID or name of the server on which the action should be performed.""",
                lookup=lookup_server_id,
            )
        )

        json_body = mapping.add_json_body(AddDisk)

        json_body.add(
            PrimitiveAttribute(
                "type",
                AddDiskType,
                required=True,
                option_name="type",
            )
        )

        json_body.add(
            PrimitiveAttribute(
                "size_gigabytes",
                int,
                required=True,
                option_name="size-gigabytes",
                description="""The size of the new disk in GB. The server must have at least this much unallocated storage space.""",
            )
        )

        json_body.add(
            PrimitiveAttribute(
                "description",
                Union[Unset, None, str],
                required=False,
                option_name="description",
                description="""An optional description for the disk. If this is null a default description will be added. Submit an empty string to prevent the default description being added.""",
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
