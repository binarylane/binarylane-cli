from ...client.api.vpc.vpc_list import sync
from ...client.client import Client
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "vpc_list"

    @property
    def description(self):
        return """List All Existing VPCs"""

    def configure(self, parser):
        """Add arguments for vpc_list"""

    def request(
        self,
        client: Client,
    ):
        return sync(
            client=client,
        )
