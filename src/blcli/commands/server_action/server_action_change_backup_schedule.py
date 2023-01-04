from typing import Any, Union

from ...client.api.server_action.server_action_change_backup_schedule import sync_detailed
from ...client.client import Client
from ...client.models.action_response import ActionResponse
from ...client.models.change_backup_schedule import ChangeBackupSchedule
from ...client.models.change_backup_schedule_type import ChangeBackupScheduleType
from ...client.models.problem_details import ProblemDetails
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...client.types import UNSET, Unset
from ...runners import CommandRunner


class Command(CommandRunner):
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
            description="""The target server id.""",
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

    def request(
        self,
        server_id: int,
        client: Client,
        type: ChangeBackupScheduleType,
        backup_hour_of_day: Union[Unset, None, int] = UNSET,
        backup_day_of_week: Union[Unset, None, int] = UNSET,
        backup_day_of_month: Union[Unset, None, int] = UNSET,
    ) -> Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]:

        return sync_detailed(
            server_id=server_id,
            client=client,
            json_body=ChangeBackupSchedule(
                type=type,
                backup_hour_of_day=backup_hour_of_day,
                backup_day_of_week=backup_day_of_week,
                backup_day_of_month=backup_day_of_month,
            ),
        ).parsed
