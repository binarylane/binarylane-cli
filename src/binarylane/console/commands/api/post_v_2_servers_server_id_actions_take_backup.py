from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Tuple, Union

from binarylane.api.server_actions.post_v_2_servers_server_id_actions_take_backup import sync_detailed
from binarylane.models.action_response import ActionResponse
from binarylane.models.backup_replacement_strategy import BackupReplacementStrategy
from binarylane.models.backup_slot import BackupSlot
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.take_backup import TakeBackup
from binarylane.models.take_backup_type import TakeBackupType
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import Unset

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import Mapping
from binarylane.console.runners.action import ActionRunner


class CommandRequest:
    server_id: int
    json_body: TakeBackup

    def __init__(self, server_id: int, json_body: TakeBackup) -> None:
        self.server_id = server_id
        self.json_body = json_body


class Command(ActionRunner):
    @property
    def name(self) -> str:
        return "take-backup"

    @property
    def description(self) -> str:
        return """Take a Backup of a Server"""

    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/ServerActions/paths/~1v2~1servers~1%7Bserver_id%7D~1actions#TakeBackup/post"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        mapping.add_primitive(
            "server_id",
            int,
            required=True,
            option_name=None,
            description="""The ID of the server on which the action should be performed.""",
        )

        json_body = mapping.add_json_body(TakeBackup)

        json_body.add_primitive(
            "type",
            TakeBackupType,
            option_name="type",
            required=True,
        )

        json_body.add_primitive(
            "replacement_strategy",
            BackupReplacementStrategy,
            option_name="replacement-strategy",
            required=True,
            description="""The strategy for selecting which backup to replace (if any).""",
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
