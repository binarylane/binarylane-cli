from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Tuple, Union

from binarylane.api.domains.get_v2_domains_domain_name_records_record_id import sync_detailed
from binarylane.models.domain_record_response import DomainRecordResponse
from binarylane.models.problem_details import ProblemDetails

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import Mapping, PrimitiveAttribute
from binarylane.console.runners.command import CommandRunner


class CommandRequest:
    domain_name: Union[int, str]
    record_id: int

    def __init__(self, domain_name: Union[int, str], record_id: int) -> None:
        self.domain_name = domain_name
        self.record_id = record_id


class Command(CommandRunner):
    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/Domains/paths/~1v2~1domains~1%7Bdomain_name%7D~1records~1%7Brecord_id%7D/get"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        mapping.add(
            PrimitiveAttribute(
                "domain_name",
                Union[int, str],
                required=True,
                option_name=None,
                description="""The domain name or domain ID for for which the record should be fetched.""",
            )
        )
        mapping.add(
            PrimitiveAttribute(
                "record_id",
                int,
                required=True,
                option_name=None,
                description="""The ID of the record to fetch.""",
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
    ) -> Tuple[HTTPStatus, Union[None, DomainRecordResponse, ProblemDetails]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.OK: DomainRecordResponse
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            domain_name=request.domain_name,
            record_id=request.record_id,
            client=client,
        )
        return page_response.status_code, page_response.parsed
