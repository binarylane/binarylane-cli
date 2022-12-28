from ...client.api.server_action.server_action_disable_backups import sync
from ...client.client import Client
from ...client.models.disable_backups import DisableBackups
from ...client.models.disable_backups_type import DisableBackupsType
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server-action_disable-backups"

    @property
    def description(self):
        return """Disable Backups for an Existing Server"""

    def configure(self, parser):
        """Add arguments for server-action_disable-backups"""
        parser.cli_argument(
            "server_id",
            description="""The target server id.""",
        )

        parser.cli_argument(
            "--type",
            dest="type",
            type=DisableBackupsType,
            required=True,
            description="""None""",
        )

    def request(
        self,
        server_id: int,
        client: Client,
        type: DisableBackupsType,
    ):
        return sync(
            server_id=server_id,
            client=client,
            json_body=DisableBackups(
                type=type,
            ),
        )
