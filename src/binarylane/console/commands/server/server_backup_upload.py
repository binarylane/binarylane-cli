from __future__ import annotations

from http import HTTPStatus
from typing import Tuple, Union

from binarylane.api.server.server_backup_upload import sync_detailed
from binarylane.client import Client
from binarylane.models.action_response import ActionResponse
from binarylane.models.backup_replacement_strategy import BackupReplacementStrategy
from binarylane.models.backup_slot import BackupSlot
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.upload_image_request import UploadImageRequest
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import UNSET, Unset

from binarylane.console.parsers import CommandParser
from binarylane.console.runners import ActionRunner


class Command(ActionRunner):
    @property
    def name(self) -> str:
        return "upload"

    @property
    def description(self) -> str:
        return """Upload a Backup for a Server"""

    def configure(self, parser: CommandParser) -> None:
        """Add arguments for server_backup_upload"""
        parser.cli_argument(
            "server_id",
            int,
            description="""The ID of the server for which the backup is to be uploaded.""",
        )

        parser.cli_argument(
            "--replacement-strategy",
            BackupReplacementStrategy,
            dest="replacement_strategy",
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
            str,
            dest="url",
            required=True,
            description="""The source URL for the image to upload. Only HTTP and HTTPS sources are currently supported.""",
        )

        parser.cli_argument(
            "--backup-type",
            Union[Unset, None, BackupSlot],
            dest="backup_type",
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
            Union[Unset, None, int],
            dest="backup_id_to_replace",
            required=False,
            description="""If replacement_strategy is 'specified' this property must be set to an existing backup.""",
        )

        parser.cli_argument(
            "--label",
            Union[Unset, None, str],
            dest="label",
            required=False,
            description="""An optional label to identify the backup.""",
        )

    @property
    def ok_response_type(self) -> type:
        return ActionResponse

    def request(
        self,
        server_id: int,
        client: Client,
        replacement_strategy: BackupReplacementStrategy,
        url: str,
        backup_type: Union[Unset, None, BackupSlot] = UNSET,
        backup_id_to_replace: Union[Unset, None, int] = UNSET,
        label: Union[Unset, None, str] = UNSET,
    ) -> Tuple[HTTPStatus, Union[ActionResponse, None, ProblemDetails, ValidationProblemDetails]]:

        # HTTPStatus.OK: ActionResponse
        # HTTPStatus.BAD_REQUEST: ValidationProblemDetails
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNPROCESSABLE_ENTITY: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            server_id=server_id,
            client=client,
            json_body=UploadImageRequest(
                replacement_strategy=replacement_strategy,
                url=url,
                backup_type=backup_type,
                backup_id_to_replace=backup_id_to_replace,
                label=label,
            ),
        )
        return page_response.status_code, page_response.parsed
