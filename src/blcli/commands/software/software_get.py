from ...client.api.software.software_get import sync
from ...client.client import Client
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "software_get"

    @property
    def description(self):
        return """Fetch Existing Software"""

    def configure(self, parser):
        """Add arguments for software_get"""
        parser.cli_argument(
            "software_id",
        )

    def request(
        self,
        software_id: str,
        client: Client,
    ):
        return sync(
            software_id=software_id,
            client=client,
        )
