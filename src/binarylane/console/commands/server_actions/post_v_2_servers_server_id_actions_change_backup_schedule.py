from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Tuple, Union

from binarylane.api.server_actions.post_v_2_servers_server_id_actions_change_backup_schedule import sync_detailed
from binarylane.models.action_response import ActionResponse
from binarylane.models.change_backup_schedule import ChangeBackupSchedule
from binarylane.models.change_backup_schedule_type import ChangeBackupScheduleType
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import Unset

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import Mapping
from binarylane.console.runners.action import ActionRunner


class CommandRequest:
    server_id: int
    json_body: ChangeBackupSchedule

    def __init__(self, server_id: int, json_body: ChangeBackupSchedule) -> None:
        self.server_id = server_id
        self.json_body = json_body


class Command(ActionRunner):
    @property
    def name(self) -> str:
        return "change-backup-schedule"

    @property
    def description(self) -> str:
        return """Change the Backup Schedule of a Server"""

    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/ServerActions/paths/~1v2~1servers~1%7Bserver_id%7D~1actions#ChangeBackupSchedule/post"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        mapping.add_primitive(
            "server_id",
            int,
            required=True,
            option_name=None,
            description="""The ID of the server on which the action should be performed.""",
        )

        json_body = mapping.add_json_body(ChangeBackupSchedule)

        json_body.add_primitive(
            "type",
            ChangeBackupScheduleType,
            option_name="type",
            required=True,
        )

        json_body.add_primitive(
            "backup_hour_of_day",
            Union[Unset, None, int],
            option_name="backup-hour-of-day",
            required=False,
            description="""Do not provide a value to keep the current setting.""",
        )

        json_body.add_primitive(
            "backup_day_of_week",
            Union[Unset, None, int],
            option_name="backup-day-of-week",
            required=False,
            description="""Sunday is 0, Monday is 1 etc. Do not provide a value to keep the current setting.""",
        )

        json_body.add_primitive(
            "backup_day_of_month",
            Union[Unset, None, int],
            option_name="backup-day-of-month",
            required=False,
            description="""Do not provide a value to keep the current setting.""",
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
