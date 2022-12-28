from ...client.api.region.region_list import sync_detailed
from ...client.client import Client
from ...client.models.regions_response import RegionsResponse
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "region_list"

    @property
    def description(self):
        return """List all Regions"""

    def configure(self, parser):
        """Add arguments for region_list"""

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

            if page_response.status_code != 200:
                return page_response.parsed

            has_next = page_response.parsed.links and page_response.parsed.links.pages.next_
            if not response:
                response = page_response.parsed
            else:
                response.regions += page_response.parsed.regions

        return response
