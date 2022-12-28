from typing import Union

from ...client.api.domain.domain_record_list import sync
from ...client.client import Client
from ...client.models.domain_record_type import DomainRecordType
from ...client.types import UNSET, Unset
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "domain_record_list"

    @property
    def description(self):
        return """List All Domain Records for a Domain"""

    def configure(self, parser):
        """Add arguments for domain_record_list"""
        parser.cli_argument(
            "domain_name",
        )

        parser.cli_argument(
            "--type",
            dest="type",
            type=Union[Unset, None, DomainRecordType],
            required=False,
            description="""
| Value | Description |
| ----- | ----------- |
| A | Map an IPv4 address to a hostname. |
| AAAA | Map an IPv6 address to a hostname. |
| CAA | Restrict which certificate authorities are permitted to issue certificates for a domain. |
| CNAME | Define an alias for your canonical hostname. |
| MX | Define the mail exchanges that handle mail for the domain. |
| NS | Define the nameservers that manage the domain. |
| SOA | The Start of Authority record for the zone. |
| SRV | Specify a server by hostname and port to handle a service or services. |
| TXT | Define a string of text that is associated with a hostname. |

""",
        )
        parser.cli_argument(
            "--name",
            dest="name",
            type=Union[Unset, None, str],
            required=False,
            description="""None""",
        )
        parser.cli_argument(
            "--page",
            dest="page",
            type=Union[Unset, None, int],
            required=False,
            description="""The selected page. Page numbering starts at 1""",
        )
        parser.cli_argument(
            "--per-page",
            dest="per_page",
            type=Union[Unset, None, int],
            required=False,
            description="""The number of results to show per page.""",
        )

    def request(
        self,
        domain_name: str,
        client: Client,
        type: Union[Unset, None, DomainRecordType] = UNSET,
        name: Union[Unset, None, str] = UNSET,
        page: Union[Unset, None, int] = 1,
        per_page: Union[Unset, None, int] = 20,
    ):
        return sync(
            domain_name=domain_name,
            client=client,
            type=type,
            name=name,
            page=page,
            per_page=per_page,
        )
