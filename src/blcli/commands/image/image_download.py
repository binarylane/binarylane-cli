from ...client.api.image.image_download import sync
from ...client.client import Client
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "image_download"

    @property
    def description(self):
        return """Download an Existing Image"""

    def configure(self, parser):
        """Add arguments for image_download"""
        parser.cli_argument(
            "image_id",
        )

    def request(
        self,
        image_id: int,
        client: Client,
    ):
        return sync(
            image_id=image_id,
            client=client,
        )
