from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Tuple, Union

from binarylane.api.domains.post_v2_domains_domain_name_records import sync_detailed
from binarylane.models.domain_record_request import DomainRecordRequest
from binarylane.models.domain_record_response import DomainRecordResponse
from binarylane.models.domain_record_type import DomainRecordType
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import Unset

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import Mapping
from binarylane.console.runners.command import CommandRunner


class CommandRequest:
    domain_name: str
    json_body: DomainRecordRequest

    def __init__(self, domain_name: str, json_body: DomainRecordRequest) -> None:
        self.domain_name = domain_name
        self.json_body = json_body


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "create"

    @property
    def description(self) -> str:
        return """Create a New Domain Record"""

    @property
    def reference_url(self) -> str:
        return (
            "https://api.binarylane.com.au/reference/#tag/Domains/paths/~1v2~1domains~1%7Bdomain_name%7D~1records/post"
        )

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        mapping.add_primitive(
            "domain_name",
            str,
            required=True,
            option_name=None,
            description="""The domain name for which the record should be created.""",
        )

        json_body = mapping.add_json_body(DomainRecordRequest)

        json_body.add_primitive(
            "type",
            Union[Unset, None, DomainRecordType],
            option_name="type",
            required=False,
            description="""The type of the DNS record.""",
        )

        json_body.add_primitive(
            "name",
            Union[Unset, None, str],
            option_name="name",
            required=False,
            description="""The subdomain for this record. Use @ for records on the domain itself, and * to create a wildcard record.""",
        )

        json_body.add_primitive(
            "data",
            Union[Unset, None, str],
            option_name="data",
            required=False,
            description="""A general data field that has different functions depending on the record type.""",
        )

        json_body.add_primitive(
            "priority",
            Union[Unset, None, int],
            option_name="priority",
            required=False,
            description="""A priority value that is only relevant for SRV and MX records.""",
        )

        json_body.add_primitive(
            "port",
            Union[Unset, None, int],
            option_name="port",
            required=False,
            description="""A port value that is only relevant for SRV records.""",
        )

        json_body.add_primitive(
            "ttl",
            Union[Unset, None, int],
            option_name="ttl",
            required=False,
            description="""This value is the time to live for the record, in seconds.""",
        )

        json_body.add_primitive(
            "weight",
            Union[Unset, None, int],
            option_name="weight",
            required=False,
            description="""The weight value that is only relevant for SRV records.""",
        )

        json_body.add_primitive(
            "flags",
            Union[Unset, None, int],
            option_name="flags",
            required=False,
            description="""An unsigned integer between 0-255 that is only relevant for CAA records.""",
        )

        json_body.add_primitive(
            "tag",
            Union[Unset, None, str],
            option_name="tag",
            required=False,
            description="""A parameter tag that is only relevant for CAA records.""",
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
            client=client,
            json_body=request.json_body,
        )
        return page_response.status_code, page_response.parsed
