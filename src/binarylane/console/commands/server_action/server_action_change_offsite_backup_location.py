from __future__ import annotations

from typing import Any, Type, Union

from binarylane.api.server_action.server_action_change_offsite_backup_location import sync_detailed
from binarylane.client import Client
from binarylane.models.action_response import ActionResponse
from binarylane.models.change_offsite_backup_location import ChangeOffsiteBackupLocation
from binarylane.models.change_offsite_backup_location_type import ChangeOffsiteBackupLocationType
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import UNSET, Unset

from binarylane.console.runners import ActionRunner


class Command(ActionRunner):
    @property
    def name(self):
        return "change-offsite-backup-location"

    @property
    def description(self):
        return """Change the Offsite Backup Location of a Server"""

    def configure(self, parser):
        """Add arguments for server-action_change-offsite-backup-location"""
        parser.cli_argument(
            "server_id",
            int,
            description="""The ID of the server on which the action should be performed.""",
        )

        parser.cli_argument(
            "--type",
            ChangeOffsiteBackupLocationType,
            dest="type",
            required=True,
            description="""None""",
        )

        parser.cli_argument(
            "--offsite-backup-location",
            Union[Unset, None, str],
            dest="offsite_backup_location",
            required=False,
            description="""Do not provide or set to null to use the internal offsite backup location, otherwise this must be a valid Amazon S3 bucket address. If this is provided Amazon will charge your S3 account at their standard rate for every backup stored.""",
        )

    @property
    def ok_response_type(self) -> Type:
        return ActionResponse

    def request(
        self,
        server_id: int,
        client: Client,
        type: ChangeOffsiteBackupLocationType,
        offsite_backup_location: Union[Unset, None, str] = UNSET,
    ) -> Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]:

        page_response = sync_detailed(
            server_id=server_id,
            client=client,
            json_body=ChangeOffsiteBackupLocation(
                type=type,
                offsite_backup_location=offsite_backup_location,
            ),
        )
        return page_response.status_code, page_response.parsed
