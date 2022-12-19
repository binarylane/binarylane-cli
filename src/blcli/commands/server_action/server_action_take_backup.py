from typing import Union

from ...client.api.server_action.server_action_take_backup import sync
from ...client.client import Client
from ...client.models.take_backup import TakeBackup
from ...client.types import UNSET, Unset
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server-action_take-backup"

    @property
    def description(self):
        return """Take a Backup of a Server"""

    def configure(self, parser):
        """Add arguments for server-action_take-backup"""
        parser.cli_argument(
            "server_id",
            description="""The target server id.""",
        )

        parser.cli_argument(
            "--type",
            dest="type",
            type=TakeBackupType,
            required=True,
            description="""None""",
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
        type: TakeBackupType,
        replacement_strategy: BackupReplacementStrategy,
        backup_type: Union[Unset, None, BackupSlot] = UNSET,
        backup_id_to_replace: Union[Unset, None, int] = UNSET,
        label: Union[Unset, None, str] = UNSET,
    ):
        return sync(
            server_id=server_id,
            client=client,
            json_body=TakeBackup(
                type=type,
                replacement_strategy=replacement_strategy,
                backup_type=backup_type,
                backup_id_to_replace=backup_id_to_replace,
                label=label,
            ),
        )
