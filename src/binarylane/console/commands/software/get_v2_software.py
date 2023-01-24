from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Dict, List, Optional, Tuple, Union

from binarylane.api.software.get_v2_software import sync_detailed
from binarylane.models.links import Links
from binarylane.models.softwares_response import SoftwaresResponse

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import Mapping
from binarylane.console.runners.list import ListRunner


class CommandRequest:
    pass


class Command(ListRunner):
    @property
    def default_format(self) -> List[str]:
        return [
            "id",
            "enabled",
            "name",
            "description",
            "cost_per_licence_per_month",
            "minimum_licence_count",
            "maximum_licence_count",
            "licence_step_count",
        ]

    @property
    def fields(self) -> Dict[str, str]:
        return {
            "id": """The ID of this software.""",
            "enabled": """Software that is not enabled is not available to be added to servers but may be retained by servers that currently use it.""",
            "name": """The name of this software.""",
            "description": """The description of this software.""",
            "cost_per_licence_per_month": """The cost for each licence of this software per month in AU$.""",
            "minimum_licence_count": """The minimum licences permitted for this software.""",
            "maximum_licence_count": """The maximum licences permitted for this software.""",
            "licence_step_count": """Licences must be purchased in multiples of this value.""",
            "supported_operating_systems": """A list of slugs of operating system images that support this software.""",
            "group": """Software in the same group may not be licensed together.""",
        }

    @property
    def name(self) -> str:
        return "list"

    @property
    def description(self) -> str:
        return """List All Available Software"""

    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/Software/paths/~1v2~1software/get"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)
        return mapping

    @property
    def ok_response_type(self) -> type:
        return SoftwaresResponse

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[None, SoftwaresResponse]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.OK: SoftwaresResponse
        page = 0
        per_page = 25
        has_next = True
        response: Optional[SoftwaresResponse] = None

        while has_next:
            page += 1
            page_response = sync_detailed(
                client=client,
                page=page,
                per_page=per_page,
            )

            status_code = page_response.status_code
            if status_code != 200:
                return status_code, page_response.parsed

            assert isinstance(page_response.parsed, SoftwaresResponse)
            has_next = isinstance(page_response.parsed.links, Links) and isinstance(
                page_response.parsed.links.pages.next_, str
            )
            if not response:
                response = page_response.parsed
            else:
                response.software += page_response.parsed.software

        return status_code, response
