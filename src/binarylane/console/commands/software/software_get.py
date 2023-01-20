from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Tuple, Union

from binarylane.api.software.software_get import sync_detailed
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.software_response import SoftwareResponse

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import Mapping
from binarylane.console.runners.command import CommandRunner


class CommandRequest:
    software_id: str

    def __init__(self, software_id: str) -> None:
        self.software_id = software_id


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "get"

    @property
    def description(self) -> str:
        return """Fetch Existing Software"""

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        mapping.add_primitive(
            "software_id",
            str,
            required=True,
            option_name=None,
            description="""The ID of the software to fetch.""",
        )

        return mapping

    @property
    def ok_response_type(self) -> type:
        return SoftwareResponse

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[None, ProblemDetails, SoftwareResponse]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.OK: SoftwareResponse
        # HTTPStatus.NOT_FOUND: ProblemDetails
        page_response = sync_detailed(
            software_id=request.software_id,
            client=client,
        )
        return page_response.status_code, page_response.parsed
