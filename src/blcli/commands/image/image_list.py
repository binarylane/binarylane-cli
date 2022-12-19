from ...client.api.image.image_list import sync
from ...client.client import Client
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "image_list"

    @property
    def description(self):
        return """List All Images"""

    def configure(self, parser):
        """Add arguments for image_list"""

    def request(
        self,
        client: Client,
    ):
        return sync(
            client=client,
        )
