from ...client.api.server_action.server_action_enable_backups import sync
from ...client.client import Client
from ...client.models.enable_backups import EnableBackups
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server-action_enable-backups"

    @property
    def description(self):
        return """Enable Two Daily Backups for an Existing Server"""

    def configure(self, parser):
        """Add arguments for server-action_enable-backups"""
        parser.cli_argument(
            "server_id",
            description="""The target server id.""",
        )

        parser.cli_argument(
            "--type",
            dest="type",
            type=EnableBackupsType,
            required=True,
            description="""None""",
        )

    def request(
        self,
        server_id: int,
        client: Client,
        type: EnableBackupsType,
    ):
        return sync(
            server_id=server_id,
            client=client,
            json_body=EnableBackups(
                type=type,
            ),
        )
