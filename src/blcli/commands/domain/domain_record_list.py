from typing import Any, Dict, List, Type, Union

from ...client.api.domain.domain_record_list import sync_detailed
from ...client.client import Client
from ...client.models.domain_record_type import DomainRecordType
from ...client.models.domain_records_response import DomainRecordsResponse
from ...client.models.problem_details import ProblemDetails
from ...client.types import UNSET, Unset
from ...runners import ListRunner


class Command(ListRunner):
    @property
    def default_format(self) -> List[str]:
        return [
            "id",
            "type",
            "name",
            "ttl",
        ]

    @property
    def fields(self) -> Dict[str, str]:
        return {
            "id": """The ID of this domain record.""",
            "type": """
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
            "name": """The subdomain, alias, or service defined by the record.""",
            "ttl": """This value is the time to live for the record in seconds.""",
            "data": """Variable data depending on record type.""",
            "priority": """A priority value that is only relevant for SRV and MX records.""",
            "port": """A port value that is only relevant for SRV records.""",
            "weight": """The weight value that is only relevant for SRV records.""",
            "flags": """An unsigned integer between 0-255 that is only relevant for CAA records.""",
            "tag": """A parameter tag that is only relevant for CAA records.""",
        }

    @property
    def name(self):
        return "list"

    @property
    def description(self):
        return """List All Domain Records for a Domain"""

    def configure(self, parser):
        """Add arguments for domain_record_list"""
        parser.cli_argument(
            "domain_name",
            type=str,
            description="""The domain name for which records should be listed.""",
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
            description="""Only return records for this subdomain name.""",
        )

    @property
    def ok_response_type(self) -> Type:
        return DomainRecordsResponse

    def request(
        self,
        domain_name: str,
        client: Client,
        type: Union[Unset, None, DomainRecordType] = UNSET,
        name: Union[Unset, None, str] = UNSET,
    ) -> Union[Any, DomainRecordsResponse, ProblemDetails]:

        page = 0
        per_page = 25
        has_next = True
        response: DomainRecordsResponse = None

        while has_next:
            page += 1
            page_response = sync_detailed(
                domain_name=domain_name,
                client=client,
                type=type,
                name=name,
                page=page,
                per_page=per_page,
            )

            status_code = page_response.status_code
            if status_code != 200:
                response = page_response.parsed
                break

            has_next = page_response.parsed.links and page_response.parsed.links.pages.next_
            if not response:
                response = page_response.parsed
            else:
                response.domain_records += page_response.parsed.domain_records

        return status_code, response
