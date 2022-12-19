from ...client.api.server.server_alert_list import sync
from ...client.client import Client
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server_alert_list"

    @property
    def description(self):
        return """List any Servers that have a Current Exceeded Threshold Alert"""

    def configure(self, parser):
        """Add arguments for server_alert_list"""

    def request(
        self,
        client: Client,
    ):
        return sync(
            client=client,
        )
