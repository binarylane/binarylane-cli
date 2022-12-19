from ...client.api.server_action.server_action_attach_backup import sync
from ...client.client import Client
from ...client.models.attach_backup import AttachBackup
from ...runner import CommandRunner


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
    ):
        return sync(
            server_id=server_id,
            client=client,
            json_body=AttachBackup(
                type=type,
                image=image,
            ),
        )
