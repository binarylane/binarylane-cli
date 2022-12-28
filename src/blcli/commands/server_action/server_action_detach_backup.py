from ...client.api.server_action.server_action_detach_backup import sync
from ...client.client import Client
from ...client.models.detach_backup import DetachBackup
from ...client.models.detach_backup_type import DetachBackupType
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server-action_detach-backup"

    @property
    def description(self):
        return """Detach Any Attached Backup from a Server"""

    def configure(self, parser):
        """Add arguments for server-action_detach-backup"""
        parser.cli_argument(
            "server_id",
            description="""The target server id.""",
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
    ):
        return sync(
            server_id=server_id,
            client=client,
            json_body=DetachBackup(
                type=type,
            ),
        )
