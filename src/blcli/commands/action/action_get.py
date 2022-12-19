from ...client.api.action.action_get import sync
from ...client.client import Client
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "action_get"

    @property
    def description(self):
        return """Fetch an Existing Action"""

    def configure(self, parser):
        """Add arguments for action_get"""
        parser.cli_argument(
            "action_id",
        )

    def request(
        self,
        action_id: int,
        client: Client,
    ):
        return sync(
            action_id=action_id,
            client=client,
        )
