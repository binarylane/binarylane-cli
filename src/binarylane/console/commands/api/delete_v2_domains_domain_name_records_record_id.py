from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Tuple, Union

from binarylane.api.domains.delete_v2_domains_domain_name_records_record_id import sync_detailed
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
        return "delete"

    @property
    def description(self) -> str:
        return """Delete an Existing Domain Record"""

    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/Domains/paths/~1v2~1domains~1%7Bdomain_name%7D~1records~1%7Brecord_id%7D/delete"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        mapping.add_primitive(
            "domain_name",
            str,
            required=True,
            option_name=None,
            description="""The domain name for which the record should be deleted.""",
        )
        mapping.add_primitive(
            "record_id",
            int,
            required=True,
            option_name=None,
            description="""The ID of the record to delete.""",
        )

        return mapping

    @property
    def ok_response_type(self) -> type:
        return type(None)

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[None, ProblemDetails]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.NO_CONTENT: Any
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            domain_name=request.domain_name,
            record_id=request.record_id,
            client=client,
        )
        return page_response.status_code, page_response.parsed
