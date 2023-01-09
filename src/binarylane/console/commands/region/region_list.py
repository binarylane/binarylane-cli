from __future__ import annotations

from typing import Dict, List, Type

from binarylane.api.region.region_list import sync_detailed
from binarylane.client import Client
from binarylane.models.regions_response import RegionsResponse

from binarylane.console.runners import ListRunner


class Command(ListRunner):
    @property
    def default_format(self) -> List[str]:
        return [
            "slug",
            "name",
            "available",
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
    def name(self):
        return "list"

    @property
    def description(self):
        return """List all Regions"""

    def configure(self, parser):
        """Add arguments for region_list"""

    @property
    def ok_response_type(self) -> Type:
        return RegionsResponse

    def request(
        self,
        client: Client,
    ) -> RegionsResponse:

        page = 0
        per_page = 25
        has_next = True
        response: RegionsResponse = None

        while has_next:
            page += 1
            page_response = sync_detailed(
                client=client,
                page=page,
                per_page=per_page,
            )

            status_code = page_response.status_code
            if status_code != 200:
                response = page_response.parsed
                break

            has_next = page_response.parsed.links and page_response.parsed.links.pages.next_
            if not response:
                response = page_response.parsed
            else:
                response.regions += page_response.parsed.regions

        return status_code, response
