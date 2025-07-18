from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Tuple, Union

from binarylane.api.domains.put_v2_domains_domain_name_records_record_id import sync_detailed
from binarylane.models.domain_record_response import DomainRecordResponse
from binarylane.models.domain_record_type import DomainRecordType
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.update_domain_record_request import UpdateDomainRecordRequest
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import Unset

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import Mapping, PrimitiveAttribute
from binarylane.console.runners.command import CommandRunner


class CommandRequest:
    domain_name: Union[int, str]
    record_id: int
    json_body: UpdateDomainRecordRequest

    def __init__(self, domain_name: Union[int, str], record_id: int, json_body: UpdateDomainRecordRequest) -> None:
        self.domain_name = domain_name
        self.record_id = record_id
        self.json_body = json_body


class Command(CommandRunner):
    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/Domains/paths/~1v2~1domains~1%7Bdomain_name%7D~1records~1%7Brecord_id%7D/put"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        mapping.add(
            PrimitiveAttribute(
                "domain_name",
                Union[int, str],
                required=True,
                option_name=None,
                description="""The domain name or domain ID for for which the record should be updated.""",
            )
        )
        mapping.add(
            PrimitiveAttribute(
                "record_id",
                int,
                required=True,
                option_name=None,
                description="""The ID of the record to update.""",
            )
        )

        json_body = mapping.add_json_body(UpdateDomainRecordRequest)

        json_body.add(
            PrimitiveAttribute(
                "type",
                Union[Unset, None, DomainRecordType],
                required=False,
                option_name="type",
                description="""The type of the DNS record.

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
        )

        json_body.add(
            PrimitiveAttribute(
                "name",
                Union[Unset, None, str],
                required=False,
                option_name="name",
                description="""The subdomain for this record. Use @ for records on the domain itself, and * to create a wildcard record.""",
            )
        )

        json_body.add(
            PrimitiveAttribute(
                "data",
                Union[Unset, None, str],
                required=False,
                option_name="data",
                description="""A general data field that has different functions depending on the record type.""",
            )
        )

        json_body.add(
            PrimitiveAttribute(
                "priority",
                Union[Unset, None, int],
                required=False,
                option_name="priority",
                description="""A priority value that is only relevant for SRV and MX records.""",
            )
        )

        json_body.add(
            PrimitiveAttribute(
                "port",
                Union[Unset, None, int],
                required=False,
                option_name="port",
                description="""A port value that is only relevant for SRV records.""",
            )
        )

        json_body.add(
            PrimitiveAttribute(
                "ttl",
                Union[Unset, None, int],
                required=False,
                option_name="ttl",
                description="""This value is the time to live for the record, in seconds.""",
            )
        )

        json_body.add(
            PrimitiveAttribute(
                "weight",
                Union[Unset, None, int],
                required=False,
                option_name="weight",
                description="""The weight value that is only relevant for SRV records.""",
            )
        )

        json_body.add(
            PrimitiveAttribute(
                "flags",
                Union[Unset, None, int],
                required=False,
                option_name="flags",
                description="""An unsigned integer between 0-255 that is only relevant for CAA records.""",
            )
        )

        json_body.add(
            PrimitiveAttribute(
                "tag",
                Union[Unset, None, str],
                required=False,
                option_name="tag",
                description="""A parameter tag that is only relevant for CAA records.""",
            )
        )

        return mapping

    @property
    def ok_response_type(self) -> type:
        return DomainRecordResponse

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[None, DomainRecordResponse, ProblemDetails, ValidationProblemDetails]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.OK: DomainRecordResponse
        # HTTPStatus.BAD_REQUEST: ValidationProblemDetails
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            domain_name=request.domain_name,
            record_id=request.record_id,
            client=client,
            json_body=request.json_body,
        )
        return page_response.status_code, page_response.parsed
