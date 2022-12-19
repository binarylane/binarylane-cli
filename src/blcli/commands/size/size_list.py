from ...client.api.size.size_list import sync
from ...client.client import Client
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "size_list"

    @property
    def description(self):
        return """List All Available Sizes"""

    def configure(self, parser):
        """Add arguments for size_list"""

    def request(
        self,
        client: Client,
    ):
        return sync(
            client=client,
        )
