from ...client.api.domain.domain_nameservers_list import sync
from ...client.client import Client
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "domain_nameservers_list"

    @property
    def description(self):
        return """List All Public Nameservers"""

    def configure(self, parser):
        """Add arguments for domain_nameservers_list"""

    def request(
        self,
        client: Client,
    ):
        return sync(
            client=client,
        )
