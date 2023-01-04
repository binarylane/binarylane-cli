from typing import Any, Union

from ...client.api.domain.domain_record_create import sync_detailed
from ...client.client import Client
from ...client.models.domain_record_request import DomainRecordRequest
from ...client.models.domain_record_response import DomainRecordResponse
from ...client.models.domain_record_type import DomainRecordType
from ...client.models.problem_details import ProblemDetails
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...client.types import UNSET, Unset
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "create"

    @property
    def description(self):
        return """Create a New Domain Record"""

    def configure(self, parser):
        """Add arguments for domain_record_create"""
        parser.cli_argument(
            "domain_name",
            type=str,
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
            description="""The subdomain for this record. Use @ for records on the domain itself, and * to create a wildcard record.""",
        )

        parser.cli_argument(
            "--data",
            dest="data",
            type=Union[Unset, None, str],
            required=False,
            description="""A general data field that has different functions depending on the record type.""",
        )

        parser.cli_argument(
            "--priority",
            dest="priority",
            type=Union[Unset, None, int],
            required=False,
            description="""A priority value that is only relevant for SRV and MX records.""",
        )

        parser.cli_argument(
            "--port",
            dest="port",
            type=Union[Unset, None, int],
            required=False,
            description="""A port value that is only relevant for SRV records.""",
        )

        parser.cli_argument(
            "--ttl",
            dest="ttl",
            type=Union[Unset, None, int],
            required=False,
            description="""This value is the time to live for the record, in seconds.""",
        )

        parser.cli_argument(
            "--weight",
            dest="weight",
            type=Union[Unset, None, int],
            required=False,
            description="""The weight value that is only relevant for SRV records.""",
        )

        parser.cli_argument(
            "--flags",
            dest="flags",
            type=Union[Unset, None, int],
            required=False,
            description="""An unsigned integer between 0-255 that is only relevant for CAA records.""",
        )

        parser.cli_argument(
            "--tag",
            dest="tag",
            type=Union[Unset, None, str],
            required=False,
            description="""A parameter tag that is only relevant for CAA records.""",
        )

    def request(
        self,
        domain_name: str,
        client: Client,
        type: Union[Unset, None, DomainRecordType] = UNSET,
        name: Union[Unset, None, str] = UNSET,
        data: Union[Unset, None, str] = UNSET,
        priority: Union[Unset, None, int] = UNSET,
        port: Union[Unset, None, int] = UNSET,
        ttl: Union[Unset, None, int] = UNSET,
        weight: Union[Unset, None, int] = UNSET,
        flags: Union[Unset, None, int] = UNSET,
        tag: Union[Unset, None, str] = UNSET,
    ) -> Union[Any, DomainRecordResponse, ProblemDetails, ValidationProblemDetails]:

        return sync_detailed(
            domain_name=domain_name,
            client=client,
            json_body=DomainRecordRequest(
                type=type,
                name=name,
                data=data,
                priority=priority,
                port=port,
                ttl=ttl,
                weight=weight,
                flags=flags,
                tag=tag,
            ),
        ).parsed
