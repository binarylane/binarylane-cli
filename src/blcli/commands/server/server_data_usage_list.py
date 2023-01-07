from typing import Any, Dict, List, Union

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
    def fields(self) -> Dict[str, str]:
        return {
            "server_id": """The ID of the server that this data transfer usage refers to.""",
            "expires": """The date and time in ISO8601 format that the current billing period expires.""",
            "transfer_gigabytes": """The included data transfer for this server in this period in GB.""",
            "current_transfer_usage_gigabytes": """The used data transfer for this server in this period in GB.
If you have more than one server, please see our data pooling policy: this value may include excess data transfer used by other servers or may have 'offloaded' excess data transfer to other servers with spare capacity.""",
            "transfer_period_end": """The date and time in ISO8601 format that the data transfer limit period ended (if it is completed) or when it will end (if this is the current period).""",
        }

    @property
    def name(self):
        return "list"

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

            status_code = page_response.status_code
            if status_code != 200:
                response = page_response.parsed
                break

            has_next = page_response.parsed.links and page_response.parsed.links.pages.next_
            if not response:
                response = page_response.parsed
            else:
                response.data_usages += page_response.parsed.data_usages

        return status_code, response
