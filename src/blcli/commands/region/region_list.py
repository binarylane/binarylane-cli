from ...client.api.region.region_list import sync
from ...client.client import Client
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "region_list"

    @property
    def description(self):
        return """List all Regions"""

    def configure(self, parser):
        """Add arguments for region_list"""

    def request(
        self,
        client: Client,
    ):
        return sync(
            client=client,
        )
