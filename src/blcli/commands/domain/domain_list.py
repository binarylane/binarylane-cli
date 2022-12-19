from ...client.api.domain.domain_list import sync
from ...client.client import Client
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "domain_list"

    @property
    def description(self):
        return """List All Domains"""

    def configure(self, parser):
        """Add arguments for domain_list"""

    def request(
        self,
        client: Client,
    ):
        return sync(
            client=client,
        )
