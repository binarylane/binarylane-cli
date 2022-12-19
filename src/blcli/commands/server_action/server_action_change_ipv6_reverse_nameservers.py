from typing import List

from ...client.api.server_action.server_action_change_ipv6_reverse_nameservers import sync
from ...client.client import Client
from ...client.models.change_ipv_6_reverse_nameservers import ChangeIpv6ReverseNameservers
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server-action_change-ipv6-reverse-nameservers"

    @property
    def description(self):
        return """Update the IPv6 Reverse Name Servers for a Server"""

    def configure(self, parser):
        """Add arguments for server-action_change-ipv6-reverse-nameservers"""
        parser.cli_argument(
            "server_id",
            description="""The target server id.""",
        )

        parser.cli_argument(
            "--type",
            dest="type",
            type=ChangeIpv6ReverseNameserversType,
            required=True,
            description="""None""",
        )

        parser.cli_argument(
            "--ipv6-reverse-nameservers",
            dest="ipv6_reverse_nameservers",
            type=List[str],
            required=True,
            description="""A list of all IPv6 reverse name servers for this server. Any existing reverse name servers that are omitted from the list will be removed from the server.""",
        )

    def request(
        self,
        server_id: int,
        client: Client,
        type: ChangeIpv6ReverseNameserversType,
        ipv6_reverse_nameservers: List[str],
    ):
        return sync(
            server_id=server_id,
            client=client,
            json_body=ChangeIpv6ReverseNameservers(
                type=type,
                ipv6_reverse_nameservers=ipv6_reverse_nameservers,
            ),
        )
