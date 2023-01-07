from typing import Any, Union

from ... import cli
from ...client.api.server_action.server_action_change_manage_offsite_backup_copies import sync_detailed
from ...client.client import Client
from ...client.models.action_response import ActionResponse
from ...client.models.change_manage_offsite_backup_copies import ChangeManageOffsiteBackupCopies
from ...client.models.change_manage_offsite_backup_copies_type import ChangeManageOffsiteBackupCopiesType
from ...client.models.problem_details import ProblemDetails
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "change-manage-offsite-backup-copies"

    @property
    def description(self):
        return """Change the Management of Offsite Backup Copies"""

    def configure(self, parser):
        """Add arguments for server-action_change-manage-offsite-backup-copies"""
        parser.cli_argument(
            "server_id",
            type=int,
            description="""The ID of the server on which the action should be performed.""",
        )

        parser.cli_argument(
            "--type",
            dest="type",
            type=ChangeManageOffsiteBackupCopiesType,
            required=True,
            description="""None""",
        )

        parser.cli_argument(
            "--manage-offsite-backup-copies",
            dest="manage_offsite_backup_copies",
            type=bool,
            required=True,
            description="""This only has effect if a custom offsite location is being used: the internal offsite backup location always manages copies. If this is true old offsite backups will be removed once the replacement upload is complete. If this is false backups must be removed from the Amazon S3 bucket manually. Amazon will charge your S3 account at their standard rate for every backup stored.""",
            action=cli.BooleanOptionalAction,
        )

    def request(
        self,
        server_id: int,
        client: Client,
        type: ChangeManageOffsiteBackupCopiesType,
        manage_offsite_backup_copies: bool,
    ) -> Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]:

        page_response = sync_detailed(
            server_id=server_id,
            client=client,
            json_body=ChangeManageOffsiteBackupCopies(
                type=type,
                manage_offsite_backup_copies=manage_offsite_backup_copies,
            ),
        )
        return page_response.status_code, page_response.parsed
