from typing import Any, Union

from ...client.api.server_action.server_action_detach_backup import sync_detailed
from ...client.client import Client
from ...client.models.action_response import ActionResponse
from ...client.models.detach_backup import DetachBackup
from ...client.models.detach_backup_type import DetachBackupType
from ...client.models.problem_details import ProblemDetails
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...runners import ActionRunner


class Command(ActionRunner):
    @property
    def name(self):
        return "detach-backup"

    @property
    def description(self):
        return """Detach Any Attached Backup from a Server"""

    def configure(self, parser):
        """Add arguments for server-action_detach-backup"""
        parser.cli_argument(
            "server_id",
            type=int,
            description="""The ID of the server on which the action should be performed.""",
        )

        parser.cli_argument(
            "--type",
            dest="type",
            type=DetachBackupType,
            required=True,
            description="""None""",
        )

    def request(
        self,
        server_id: int,
        client: Client,
        type: DetachBackupType,
    ) -> Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]:

        page_response = sync_detailed(
            server_id=server_id,
            client=client,
            json_body=DetachBackup(
                type=type,
            ),
        )
        return page_response.status_code, page_response.parsed
