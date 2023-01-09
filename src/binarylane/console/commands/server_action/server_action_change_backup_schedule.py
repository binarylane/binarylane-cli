from __future__ import annotations

from typing import Any, Type, Union

from binarylane.api.server_action.server_action_change_backup_schedule import sync_detailed
from binarylane.client import Client
from binarylane.models.action_response import ActionResponse
from binarylane.models.change_backup_schedule import ChangeBackupSchedule
from binarylane.models.change_backup_schedule_type import ChangeBackupScheduleType
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import UNSET, Unset

from binarylane.console.runners import ActionRunner


class Command(ActionRunner):
    @property
    def name(self):
        return "change-backup-schedule"

    @property
    def description(self):
        return """Change the Backup Schedule of a Server"""

    def configure(self, parser):
        """Add arguments for server-action_change-backup-schedule"""
        parser.cli_argument(
            "server_id",
            type=int,
            description="""The ID of the server on which the action should be performed.""",
        )

        parser.cli_argument(
            "--type",
            dest="type",
            type=ChangeBackupScheduleType,
            required=True,
            description="""None""",
        )

        parser.cli_argument(
            "--backup-hour-of-day",
            dest="backup_hour_of_day",
            type=Union[Unset, None, int],
            required=False,
            description="""Do not provide a value to keep the current setting.""",
        )

        parser.cli_argument(
            "--backup-day-of-week",
            dest="backup_day_of_week",
            type=Union[Unset, None, int],
            required=False,
            description="""Sunday is 0, Monday is 1 etc. Do not provide a value to keep the current setting.""",
        )

        parser.cli_argument(
            "--backup-day-of-month",
            dest="backup_day_of_month",
            type=Union[Unset, None, int],
            required=False,
            description="""Do not provide a value to keep the current setting.""",
        )

    @property
    def ok_response_type(self) -> Type:
        return ActionResponse

    def request(
        self,
        server_id: int,
        client: Client,
        type: ChangeBackupScheduleType,
        backup_hour_of_day: Union[Unset, None, int] = UNSET,
        backup_day_of_week: Union[Unset, None, int] = UNSET,
        backup_day_of_month: Union[Unset, None, int] = UNSET,
    ) -> Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]:

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
