from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Tuple, Union

from binarylane.api.server_actions.post_v_2_servers_server_id_actions_change_manage_offsite_backup_copies import (
    sync_detailed,
)
from binarylane.models.action_response import ActionResponse
from binarylane.models.change_manage_offsite_backup_copies import ChangeManageOffsiteBackupCopies
from binarylane.models.change_manage_offsite_backup_copies_type import ChangeManageOffsiteBackupCopiesType
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import Mapping
from binarylane.console.runners.action import ActionRunner


class CommandRequest:
    server_id: int
    json_body: ChangeManageOffsiteBackupCopies

    def __init__(self, server_id: int, json_body: ChangeManageOffsiteBackupCopies) -> None:
        self.server_id = server_id
        self.json_body = json_body


class Command(ActionRunner):
    @property
    def name(self) -> str:
        return "change-manage-offsite-backup-copies"

    @property
    def description(self) -> str:
        return """Change the Management of Offsite Backup Copies"""

    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/ServerActions/paths/~1v2~1servers~1%7Bserver_id%7D~1actions#ChangeManageOffsiteBackupCopies/post"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        mapping.add_primitive(
            "server_id",
            int,
            required=True,
            option_name=None,
            description="""The ID of the server on which the action should be performed.""",
        )

        json_body = mapping.add_json_body(ChangeManageOffsiteBackupCopies)

        json_body.add_primitive(
            "type",
            ChangeManageOffsiteBackupCopiesType,
            option_name="type",
            required=True,
        )

        json_body.add_primitive(
            "manage_offsite_backup_copies",
            bool,
            option_name="manage-offsite-backup-copies",
            required=True,
            description="""This only has effect if a custom offsite location is being used: the internal offsite backup location always manages copies. If this is true old offsite backups will be removed once the replacement upload is complete. If this is false backups must be removed from the Amazon S3 bucket manually. Amazon will charge your S3 account at their standard rate for every backup stored.""",
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
