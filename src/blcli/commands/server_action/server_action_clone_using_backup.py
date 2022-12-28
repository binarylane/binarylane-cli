from typing import Any, Union

from ...client.api.server_action.server_action_clone_using_backup import sync_detailed
from ...client.client import Client
from ...client.models.action_response import ActionResponse
from ...client.models.clone_using_backup import CloneUsingBackup
from ...client.models.clone_using_backup_type import CloneUsingBackupType
from ...client.models.problem_details import ProblemDetails
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...client.types import UNSET, Unset
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server-action_clone-using-backup"

    @property
    def description(self):
        return """Restore a Backup of a Server to a Different Existing Server"""

    def configure(self, parser):
        """Add arguments for server-action_clone-using-backup"""
        parser.cli_argument(
            "server_id",
            description="""The target server id.""",
        )

        parser.cli_argument(
            "--type",
            dest="type",
            type=CloneUsingBackupType,
            required=True,
            description="""None""",
        )

        parser.cli_argument(
            "--image-id",
            dest="image_id",
            type=int,
            required=True,
            description="""The ID of the image to clone. Only backup type images are currently supported. This must be a backup of the server ID in the action endpoint URL.""",
        )

        parser.cli_argument(
            "--target-server-id",
            dest="target_server_id",
            type=int,
            required=True,
            description="""The target server ID. This server's current disks will be wiped and replaced with the selected backup image.""",
        )

        parser.cli_argument(
            "--name",
            dest="name",
            type=Union[Unset, None, str],
            required=False,
            description="""The new hostname for the target server. If this is not supplied the target server's existing hostname will be used.""",
        )

    def request(
        self,
        server_id: int,
        client: Client,
        type: CloneUsingBackupType,
        image_id: int,
        target_server_id: int,
        name: Union[Unset, None, str] = UNSET,
    ) -> Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]:

        return sync_detailed(
            server_id=server_id,
            client=client,
            json_body=CloneUsingBackup(
                type=type,
                image_id=image_id,
                target_server_id=target_server_id,
                name=name,
            ),
        ).parsed
