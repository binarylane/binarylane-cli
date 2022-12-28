from typing import Any, List, Union

from ...client.api.server.server_data_usage_list import sync_detailed
from ...client.client import Client
from ...client.models.data_usages_response import DataUsagesResponse
from ...runners import ListRunner


class Command(ListRunner):
    @property
    def default_format(self) -> List[str]:
        return [
            "server_id",
            "expires",
            "transfer_gigabytes",
            "current_transfer_usage_gigabytes",
            "transfer_period_end",
        ]

    @property
    def name(self):
        return "server_data-usage_list"

    @property
    def description(self):
        return """Fetch all Current Data Usage (Transfer) for All Servers"""

    def configure(self, parser):
        """Add arguments for server_data-usage_list"""

    def request(
        self,
        client: Client,
    ) -> Union[Any, DataUsagesResponse]:

        page = 0
        per_page = 25
        has_next = True
        response: DataUsagesResponse = None

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
                response.data_usages += page_response.parsed.data_usages

        return response
