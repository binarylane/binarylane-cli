from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Tuple, Union

from binarylane.api.servers.post_v2_servers_server_id_backups import sync_detailed
from binarylane.models.action_response import ActionResponse
from binarylane.models.backup_replacement_strategy import BackupReplacementStrategy
from binarylane.models.backup_slot import BackupSlot
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.upload_image_request import UploadImageRequest
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import Unset

if TYPE_CHECKING:
    from binarylane.client import Client

import binarylane.console.commands.api.get_v2_servers as api_get_v2_servers
from binarylane.console.parser import Mapping, PrimitiveAttribute
from binarylane.console.runners.action import ActionRunner


class CommandRequest:
    server_id: int
    json_body: UploadImageRequest

    def __init__(self, server_id: int, json_body: UploadImageRequest) -> None:
        self.server_id = server_id
        self.json_body = json_body


class Command(ActionRunner):
    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/Servers/paths/~1v2~1servers~1%7Bserver_id%7D~1backups/post"

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
                description="""The ID or name of the server for which the backup is to be uploaded.""",
                lookup=lookup_server_id,
            )
        )

        json_body = mapping.add_json_body(UploadImageRequest)

        json_body.add(
            PrimitiveAttribute(
                "replacement_strategy",
                BackupReplacementStrategy,
                required=True,
                option_name="replacement-strategy",
                description="""The strategy for selecting which backup to replace (if any).

| Value | Description |
| ----- | ----------- |
| none | Do not replace any existing backup: use a free slot of the provided backup type. If there are no free slots an error will occur. |
| specified | Replace the specific backup id provided. |
| oldest | Use any free slots of the provided backup type, and if there are no free slots replace the oldest unlocked and un-attached backup of the provided backup type. |
| newest | Use any free slots of the provided backup type, and if there are no free slots replace the newest unlocked and un-attached backup of the provided backup type. |

""",
            )
        )

        json_body.add(
            PrimitiveAttribute(
                "url",
                str,
                required=True,
                option_name="url",
                description="""The source URL for the image to upload. Only HTTP and HTTPS sources are currently supported.""",
            )
        )

        json_body.add(
            PrimitiveAttribute(
                "backup_type",
                Union[Unset, None, BackupSlot],
                required=False,
                option_name="backup-type",
                description="""If replacement_strategy is anything other than 'specified', this must be provided.

| Value | Description |
| ----- | ----------- |
| daily | A backup which is scheduled to be taken each day. |
| weekly | A backup which is scheduled to be taken each week. |
| monthly | A backup which is scheduled to be taken each month. |
| temporary | A backup which is created on demand and only retained for a maximum of seven days. |

""",
            )
        )

        json_body.add(
            PrimitiveAttribute(
                "backup_id_to_replace",
                Union[Unset, None, int],
                required=False,
                option_name="backup-id-to-replace",
                description="""If replacement_strategy is 'specified' this property must be set to an existing backup.""",
            )
        )

        json_body.add(
            PrimitiveAttribute(
                "label",
                Union[Unset, None, str],
                required=False,
                option_name="label",
                description="""An optional label to identify the backup.""",
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
        # HTTPStatus.BAD_REQUEST: ValidationProblemDetails
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            server_id=request.server_id,
            client=client,
            json_body=request.json_body,
        )
        return page_response.status_code, page_response.parsed
