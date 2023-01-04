from typing import Any, Union

from ...client.api.server_action.server_action_change_offsite_backup_location import sync_detailed
from ...client.client import Client
from ...client.models.action_response import ActionResponse
from ...client.models.change_offsite_backup_location import ChangeOffsiteBackupLocation
from ...client.models.change_offsite_backup_location_type import ChangeOffsiteBackupLocationType
from ...client.models.problem_details import ProblemDetails
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...client.types import UNSET, Unset
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server-action_change-offsite-backup-location"

    @property
    def description(self):
        return """Change the Offsite Backup Location of a Server"""

    def configure(self, parser):
        """Add arguments for server-action_change-offsite-backup-location"""
        parser.cli_argument(
            "server_id",
            type=int,
            description="""The target server id.""",
        )

        parser.cli_argument(
            "--type",
            dest="type",
            type=ChangeOffsiteBackupLocationType,
            required=True,
            description="""None""",
        )

        parser.cli_argument(
            "--offsite-backup-location",
            dest="offsite_backup_location",
            type=Union[Unset, None, str],
            required=False,
            description="""Do not provide or set to null to use the internal offsite backup location, otherwise this must be a valid Amazon S3 bucket address. If this is provided Amazon will charge your S3 account at their standard rate for every backup stored.""",
        )

    def request(
        self,
        server_id: int,
        client: Client,
        type: ChangeOffsiteBackupLocationType,
        offsite_backup_location: Union[Unset, None, str] = UNSET,
    ) -> Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]:

        return sync_detailed(
            server_id=server_id,
            client=client,
            json_body=ChangeOffsiteBackupLocation(
                type=type,
                offsite_backup_location=offsite_backup_location,
            ),
        ).parsed
