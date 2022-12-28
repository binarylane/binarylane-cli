from typing import Any, Union

from ...client.api.vpc.vpc_list import sync_detailed
from ...client.client import Client
from ...client.models.vpcs_response import VpcsResponse
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "vpc_list"

    @property
    def description(self):
        return """List All Existing VPCs"""

    def configure(self, parser):
        """Add arguments for vpc_list"""

    def request(
        self,
        client: Client,
    ) -> Union[Any, VpcsResponse]:

        page = 0
        per_page = 25
        has_next = True
        response: VpcsResponse = None

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
                response.vpcs += page_response.parsed.vpcs

        return response
