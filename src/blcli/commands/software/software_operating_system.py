from ...client.api.software.software_operating_system import sync
from ...client.client import Client
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "software_operating-system"

    @property
    def description(self):
        return """List All Available Software for an Existing Operating System"""

    def configure(self, parser):
        """Add arguments for software_operating-system"""
        parser.cli_argument(
            "operating_system_id_or_slug",
        )

    def request(
        self,
        operating_system_id_or_slug: str,
        client: Client,
    ):
        return sync(
            operating_system_id_or_slug=operating_system_id_or_slug,
            client=client,
        )
