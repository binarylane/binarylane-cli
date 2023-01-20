from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Tuple, Union

from binarylane.api.server_action.server_action_clone_using_backup import sync_detailed
from binarylane.models.action_response import ActionResponse
from binarylane.models.clone_using_backup import CloneUsingBackup
from binarylane.models.clone_using_backup_type import CloneUsingBackupType
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import Unset

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import Mapping
from binarylane.console.runners import ActionRunner


class CommandRequest:
    server_id: int
    json_body: CloneUsingBackup

    def __init__(self, server_id: int, json_body: CloneUsingBackup) -> None:
        self.server_id = server_id
        self.json_body = json_body


class Command(ActionRunner):
    @property
    def name(self) -> str:
        return "clone-using-backup"

    @property
    def description(self) -> str:
        return """Restore a Backup of a Server to a Different Existing Server"""

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        mapping.add_primitive(
            "server_id",
            int,
            required=True,
            option_name=None,
            description="""The ID of the server on which the action should be performed.""",
        )

        json_body = mapping.add_json_body(CloneUsingBackup)

        json_body.add_primitive(
            "type",
            CloneUsingBackupType,
            option_name="type",
            required=True,
        )

        json_body.add_primitive(
            "image_id",
            int,
            option_name="image-id",
            required=True,
            description="""The ID of the image to clone. Only backup type images are currently supported. This must be a backup of the server ID in the action endpoint URL.""",
        )

        json_body.add_primitive(
            "target_server_id",
            int,
            option_name="target-server-id",
            required=True,
            description="""The target server ID. This server's current disks will be wiped and replaced with the selected backup image.""",
        )

        json_body.add_primitive(
            "name",
            Union[Unset, None, str],
            option_name="name",
            required=False,
            description="""The new hostname for the target server. If this is not supplied the target server's existing hostname will be used.""",
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
