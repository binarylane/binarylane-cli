from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Dict, List, Optional, Tuple, Union

from binarylane.api.regions.get_v2_regions import sync_detailed
from binarylane.models.links import Links
from binarylane.models.regions_response import RegionsResponse

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
            "slug",
            "name",
        ]

    @property
    def fields(self) -> Dict[str, str]:
        return {
            "slug": """The unique slug for this region.""",
            "name": """The name of this region.""",
            "sizes": """The slugs of the sizes available in this region.""",
            "available": """Whether this region is available for the allocation of new resources.""",
            "features": """A list of features available for resources in this region.""",
            "name_servers": """A list of nameservers available for resources in this region.""",
        }

    @property
    def name(self) -> str:
        return "list"

    @property
    def description(self) -> str:
        return """List all Regions"""

    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/Regions/paths/~1v2~1regions/get"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)
        return mapping

    @property
    def ok_response_type(self) -> type:
        return RegionsResponse

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[None, RegionsResponse]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.OK: RegionsResponse
        page = 0
        per_page = 25
        has_next = True
        response: Optional[RegionsResponse] = None

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

            assert isinstance(page_response.parsed, RegionsResponse)
            has_next = isinstance(page_response.parsed.links, Links) and isinstance(
                page_response.parsed.links.pages.next_, str
            )
            if not response:
                response = page_response.parsed
            else:
                response.regions += page_response.parsed.regions

        return status_code, response
