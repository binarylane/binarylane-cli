from typing import Any

from ...client.api.domain.domain_refresh_nameserver_cache import sync_detailed
from ...client.client import Client
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "refresh-nameserver-cache"

    @property
    def description(self):
        return """Refresh Cached Nameserver Domain Records"""

    def configure(self, parser):
        """Add arguments for domain_refresh-nameserver-cache"""

    def request(
        self,
        client: Client,
    ) -> Any:

        return sync_detailed(
            client=client,
        ).parsed
