from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Tuple, Union

from binarylane.api.software.get_v2_software_software_id import sync_detailed
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

    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/Software/paths/~1v2~1software~1%7Bsoftware_id%7D/get"

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
