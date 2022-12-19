from ...client.api.server.server_ipv6_ptr_ns_list import sync
from ...client.client import Client
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server_ipv6-ptr-ns_list"

    @property
    def description(self):
        return """Fetch all Existing IPv6 Name Server Records"""

    def configure(self, parser):
        """Add arguments for server_ipv6-ptr-ns_list"""

    def request(
        self,
        client: Client,
    ):
        return sync(
            client=client,
        )
