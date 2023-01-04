from typing import Any, Union

from ...client.api.server_action.server_action_attach_backup import sync_detailed
from ...client.client import Client
from ...client.models.action_response import ActionResponse
from ...client.models.attach_backup import AttachBackup
from ...client.models.attach_backup_type import AttachBackupType
from ...client.models.problem_details import ProblemDetails
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server-action_attach-backup"

    @property
    def description(self):
        return """Attach a Backup to a Server"""

    def configure(self, parser):
        """Add arguments for server-action_attach-backup"""
        parser.cli_argument(
            "server_id",
            type=int,
            description="""The target server id.""",
        )

        parser.cli_argument(
            "--type",
            dest="type",
            type=AttachBackupType,
            required=True,
            description="""None""",
        )

        parser.cli_argument(
            "--image",
            dest="image",
            type=int,
            required=True,
            description="""Only attaching backup images is currently supported.""",
        )

    def request(
        self,
        server_id: int,
        client: Client,
        type: AttachBackupType,
        image: int,
    ) -> Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]:

        return sync_detailed(
            server_id=server_id,
            client=client,
            json_body=AttachBackup(
                type=type,
                image=image,
            ),
        ).parsed
