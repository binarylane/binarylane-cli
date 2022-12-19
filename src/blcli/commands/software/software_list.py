from ...client.api.software.software_list import sync
from ...client.client import Client
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "software_list"

    @property
    def description(self):
        return """List All Available Software"""

    def configure(self, parser):
        """Add arguments for software_list"""

    def request(
        self,
        client: Client,
    ):
        return sync(
            client=client,
        )
