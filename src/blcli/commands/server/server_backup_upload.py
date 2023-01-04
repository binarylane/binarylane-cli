from typing import Any, Union

from ...client.api.server.server_backup_upload import sync_detailed
from ...client.client import Client
from ...client.models.action_response import ActionResponse
from ...client.models.backup_replacement_strategy import BackupReplacementStrategy
from ...client.models.backup_slot import BackupSlot
from ...client.models.problem_details import ProblemDetails
from ...client.models.upload_image_request import UploadImageRequest
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...client.types import UNSET, Unset
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "upload"

    @property
    def description(self):
        return """Upload a Backup for a Server"""

    def configure(self, parser):
        """Add arguments for server_backup_upload"""
        parser.cli_argument(
            "server_id",
            type=int,
            description="""The target server id.""",
        )

        parser.cli_argument(
            "--replacement-strategy",
            dest="replacement_strategy",
            type=BackupReplacementStrategy,
            required=True,
            description="""
| Value | Description |
| ----- | ----------- |
| none | Do not replace any existing backup: use a free slot of the provided backup type. If there are no free slots an error will occur. |
| specified | Replace the specific backup id provided. |
| oldest | Use any free slots of the provided backup type, and if there are no free slots replace the oldest unlocked and un-attached backup of the provided backup type. |
| newest | Use any free slots of the provided backup type, and if there are no free slots replace the newest unlocked and un-attached backup of the provided backup type. |

""",
        )

        parser.cli_argument(
            "--url",
            dest="url",
            type=str,
            required=True,
            description="""The source URL for the image to upload. Only HTTP and HTTPS sources are currently supported.""",
        )

        parser.cli_argument(
            "--backup-type",
            dest="backup_type",
            type=Union[Unset, None, BackupSlot],
            required=False,
            description="""
| Value | Description |
| ----- | ----------- |
| daily | A backup which is scheduled to be taken each day. |
| weekly | A backup which is scheduled to be taken each week. |
| monthly | A backup which is scheduled to be taken each month. |
| temporary | A backup which is created on demand and only retained for a maximum of seven days. |

""",
        )

        parser.cli_argument(
            "--backup-id-to-replace",
            dest="backup_id_to_replace",
            type=Union[Unset, None, int],
            required=False,
            description="""If replacement_strategy is 'specified' this property must be set to an existing backup.""",
        )

        parser.cli_argument(
            "--label",
            dest="label",
            type=Union[Unset, None, str],
            required=False,
            description="""An optional label to identify the backup.""",
        )

    def request(
        self,
        server_id: int,
        client: Client,
        replacement_strategy: BackupReplacementStrategy,
        url: str,
        backup_type: Union[Unset, None, BackupSlot] = UNSET,
        backup_id_to_replace: Union[Unset, None, int] = UNSET,
        label: Union[Unset, None, str] = UNSET,
    ) -> Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]:

        return sync_detailed(
            server_id=server_id,
            client=client,
            json_body=UploadImageRequest(
                replacement_strategy=replacement_strategy,
                url=url,
                backup_type=backup_type,
                backup_id_to_replace=backup_id_to_replace,
                label=label,
            ),
        ).parsed
