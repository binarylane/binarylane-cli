from ...client.api.action.action_list import sync
from ...client.client import Client
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "action_list"

    @property
    def description(self):
        return """List All Actions"""

    def configure(self, parser):
        """Add arguments for action_list"""

    def request(
        self,
        client: Client,
    ):
        return sync(
            client=client,
        )
