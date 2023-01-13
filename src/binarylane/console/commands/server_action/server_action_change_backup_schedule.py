from __future__ import annotations

from http import HTTPStatus
from typing import Tuple, Union

from binarylane.api.server_action.server_action_change_backup_schedule import sync_detailed
from binarylane.client import Client
from binarylane.models.action_response import ActionResponse
from binarylane.models.change_backup_schedule import ChangeBackupSchedule
from binarylane.models.change_backup_schedule_type import ChangeBackupScheduleType
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import UNSET, Unset

from binarylane.console.parsers import CommandParser
from binarylane.console.runners import ActionRunner


class Command(ActionRunner):
    @property
    def name(self) -> str:
        return "change-backup-schedule"

    @property
    def description(self) -> str:
        return """Change the Backup Schedule of a Server"""

    def configure(self, parser: CommandParser) -> None:
        """Add arguments for server-action_change-backup-schedule"""
        parser.cli_argument(
            "server_id",
            int,
            description="""The ID of the server on which the action should be performed.""",
        )

        parser.cli_argument(
            "--type",
            ChangeBackupScheduleType,
            dest="type",
            required=True,
            description="""None""",
        )

        parser.cli_argument(
            "--backup-hour-of-day",
            Union[Unset, None, int],
            dest="backup_hour_of_day",
            required=False,
            description="""Do not provide a value to keep the current setting.""",
        )

        parser.cli_argument(
            "--backup-day-of-week",
            Union[Unset, None, int],
            dest="backup_day_of_week",
            required=False,
            description="""Sunday is 0, Monday is 1 etc. Do not provide a value to keep the current setting.""",
        )

        parser.cli_argument(
            "--backup-day-of-month",
            Union[Unset, None, int],
            dest="backup_day_of_month",
            required=False,
            description="""Do not provide a value to keep the current setting.""",
        )

    @property
    def ok_response_type(self) -> type:
        return ActionResponse

    def request(
        self,
        server_id: int,
        client: Client,
        type: ChangeBackupScheduleType,
        backup_hour_of_day: Union[Unset, None, int] = UNSET,
        backup_day_of_week: Union[Unset, None, int] = UNSET,
        backup_day_of_month: Union[Unset, None, int] = UNSET,
    ) -> Tuple[HTTPStatus, Union[ActionResponse, None, ProblemDetails, ValidationProblemDetails]]:

        # HTTPStatus.OK: ActionResponse
        # HTTPStatus.ACCEPTED: Any
        # HTTPStatus.BAD_REQUEST: ValidationProblemDetails
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNPROCESSABLE_ENTITY: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            server_id=server_id,
            client=client,
            json_body=ChangeBackupSchedule(
                type=type,
                backup_hour_of_day=backup_hour_of_day,
                backup_day_of_week=backup_day_of_week,
                backup_day_of_month=backup_day_of_month,
            ),
        )
        return page_response.status_code, page_response.parsed
