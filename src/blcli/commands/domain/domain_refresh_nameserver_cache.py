from ...client.api.domain.domain_refresh_nameserver_cache import sync
from ...client.client import Client
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "domain_refresh-nameserver-cache"

    @property
    def description(self):
        return """Refresh Cached Nameserver Domain Records"""

    def configure(self, parser):
        """Add arguments for domain_refresh-nameserver-cache"""

    def request(
        self,
        client: Client,
    ):
        return sync(
            client=client,
        )
