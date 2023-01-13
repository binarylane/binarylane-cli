from __future__ import annotations

from http import HTTPStatus
from typing import Tuple, Union

from binarylane.api.domain.domain_record_update import sync_detailed
from binarylane.client import Client
from binarylane.models.domain_record_request import DomainRecordRequest
from binarylane.models.domain_record_response import DomainRecordResponse
from binarylane.models.domain_record_type import DomainRecordType
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import UNSET, Unset

from binarylane.console.parsers import CommandParser
from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "update"

    @property
    def description(self) -> str:
        return """Update an Existing Domain Record"""

    def configure(self, parser: CommandParser) -> None:
        """Add arguments for domain_record_update"""
        parser.cli_argument(
            "domain_name",
            str,
            description="""The domain name for which the record should be updated.""",
        )
        parser.cli_argument(
            "record_id",
            int,
            description="""The ID of the record to update.""",
        )

        parser.cli_argument(
            "--type",
            Union[Unset, None, DomainRecordType],
            dest="type",
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
            Union[Unset, None, str],
            dest="name",
            required=False,
            description="""The subdomain for this record. Use @ for records on the domain itself, and * to create a wildcard record.""",
        )

        parser.cli_argument(
            "--data",
            Union[Unset, None, str],
            dest="data",
            required=False,
            description="""A general data field that has different functions depending on the record type.""",
        )

        parser.cli_argument(
            "--priority",
            Union[Unset, None, int],
            dest="priority",
            required=False,
            description="""A priority value that is only relevant for SRV and MX records.""",
        )

        parser.cli_argument(
            "--port",
            Union[Unset, None, int],
            dest="port",
            required=False,
            description="""A port value that is only relevant for SRV records.""",
        )

        parser.cli_argument(
            "--ttl",
            Union[Unset, None, int],
            dest="ttl",
            required=False,
            description="""This value is the time to live for the record, in seconds.""",
        )

        parser.cli_argument(
            "--weight",
            Union[Unset, None, int],
            dest="weight",
            required=False,
            description="""The weight value that is only relevant for SRV records.""",
        )

        parser.cli_argument(
            "--flags",
            Union[Unset, None, int],
            dest="flags",
            required=False,
            description="""An unsigned integer between 0-255 that is only relevant for CAA records.""",
        )

        parser.cli_argument(
            "--tag",
            Union[Unset, None, str],
            dest="tag",
            required=False,
            description="""A parameter tag that is only relevant for CAA records.""",
        )

    @property
    def ok_response_type(self) -> type:
        return DomainRecordResponse

    def request(
        self,
        domain_name: str,
        record_id: int,
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
    ) -> Tuple[HTTPStatus, Union[None, DomainRecordResponse, ProblemDetails, ValidationProblemDetails]]:

        # HTTPStatus.OK: DomainRecordResponse
        # HTTPStatus.BAD_REQUEST: ValidationProblemDetails
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            domain_name=domain_name,
            record_id=record_id,
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
        )
        return page_response.status_code, page_response.parsed
