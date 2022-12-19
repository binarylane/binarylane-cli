from ...client.api.image.image_get import sync
from ...client.client import Client
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "image_get"

    @property
    def description(self):
        return """Fetch an Existing Image"""

    def configure(self, parser):
        """Add arguments for image_get"""
        parser.cli_argument(
            "image_id_or_slug",
        )

    def request(
        self,
        image_id_or_slug: str,
        client: Client,
    ):
        return sync(
            image_id_or_slug=image_id_or_slug,
            client=client,
        )
