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

from binarylane.console.parser import Mapping
from binarylane.console.runners.action import ActionRunner


class CommandRequest:
    server_id: int
    json_body: UploadImageRequest

    def __init__(self, server_id: int, json_body: UploadImageRequest) -> None:
        self.server_id = server_id
        self.json_body = json_body


class Command(ActionRunner):
    @property
    def name(self) -> str:
        return "upload"

    @property
    def description(self) -> str:
        return """Upload a Backup for a Server"""

    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/Servers/paths/~1v2~1servers~1%7Bserver_id%7D~1backups/post"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        mapping.add_primitive(
            "server_id",
            int,
            required=True,
            option_name=None,
            description="""The ID of the server for which the backup is to be uploaded.""",
        )

        json_body = mapping.add_json_body(UploadImageRequest)

        json_body.add_primitive(
            "replacement_strategy",
            BackupReplacementStrategy,
            option_name="replacement-strategy",
            required=True,
            description="""The strategy for selecting which backup to replace (if any).""",
        )

        json_body.add_primitive(
            "url",
            str,
            option_name="url",
            required=True,
            description="""The source URL for the image to upload. Only HTTP and HTTPS sources are currently supported.""",
        )

        json_body.add_primitive(
            "backup_type",
            Union[Unset, None, BackupSlot],
            option_name="backup-type",
            required=False,
            description="""If replacement_strategy is anything other than 'specified', this must be provided.""",
        )

        json_body.add_primitive(
            "backup_id_to_replace",
            Union[Unset, None, int],
            option_name="backup-id-to-replace",
            required=False,
            description="""If replacement_strategy is 'specified' this property must be set to an existing backup.""",
        )

        json_body.add_primitive(
            "label",
            Union[Unset, None, str],
            option_name="label",
            required=False,
            description="""An optional label to identify the backup.""",
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
        # HTTPStatus.UNPROCESSABLE_ENTITY: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            server_id=request.server_id,
            client=client,
            json_body=request.json_body,
        )
        return page_response.status_code, page_response.parsed
