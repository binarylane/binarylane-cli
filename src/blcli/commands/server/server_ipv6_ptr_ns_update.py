from typing import List, Union

from ...client.api.server.server_ipv6_ptr_ns_update import sync
from ...client.client import Client
from ...client.models.reverse_nameservers_request import ReverseNameserversRequest
from ...client.types import UNSET, Unset
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server_ipv6-ptr-ns_update"

    @property
    def description(self):
        return """Create New or Update Existing IPv6 Name Server Records"""

    def configure(self, parser):
        """Add arguments for server_ipv6-ptr-ns_update"""

        parser.cli_argument(
            "--reverse-nameservers",
            dest="reverse_nameservers",
            type=Union[Unset, None, List[str]],
            required=False,
            description="""A list of all IPv6 reverse name servers for this server. Any existing reverse name servers that are omitted from the list will be removed from the server.""",
        )

    def request(
        self,
        client: Client,
        reverse_nameservers: Union[Unset, None, List[str]] = UNSET,
    ):
        return sync(
            client=client,
            json_body=ReverseNameserversRequest(
                reverse_nameservers=reverse_nameservers,
            ),
        )
