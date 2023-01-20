from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Tuple, Union

from binarylane.api.domain.domain_record_get import sync_detailed
from binarylane.models.domain_record_response import DomainRecordResponse
from binarylane.models.problem_details import ProblemDetails

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import Mapping
from binarylane.console.runners.command import CommandRunner


class CommandRequest:
    domain_name: str
    record_id: int

    def __init__(self, domain_name: str, record_id: int) -> None:
        self.domain_name = domain_name
        self.record_id = record_id


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "get"

    @property
    def description(self) -> str:
        return """Fetch an Existing Domain Record"""

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        mapping.add_primitive(
            "domain_name",
            str,
            required=True,
            option_name=None,
            description="""The domain name for which the record should be fetched.""",
        )
        mapping.add_primitive(
            "record_id",
            int,
            required=True,
            option_name=None,
            description="""The ID of the record to fetch.""",
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
