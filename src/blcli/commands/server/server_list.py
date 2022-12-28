from typing import Any, Union

from ...client.api.server.server_list import sync_detailed
from ...client.client import Client
from ...client.models.servers_response import ServersResponse
from ...client.types import UNSET, Unset
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server_list"

    @property
    def description(self):
        return """List All Servers"""

    def configure(self, parser):
        """Add arguments for server_list"""

        parser.cli_argument(
            "--tag-name",
            dest="tag_name",
            type=Union[Unset, None, str],
            required=False,
            description="""None""",
        )

    def request(
        self,
        client: Client,
        tag_name: Union[Unset, None, str] = UNSET,
    ) -> Union[Any, ServersResponse]:

        page = 0
        per_page = 25
        has_next = True
        response: ServersResponse = None

        while has_next:
            page += 1
            page_response = sync_detailed(
                client=client,
                tag_name=tag_name,
                page=page,
                per_page=per_page,
            )

            if page_response.status_code != 200:
                return page_response.parsed

            has_next = page_response.parsed.links and page_response.parsed.links.pages.next_
            if not response:
                response = page_response.parsed
            else:
                response.servers += page_response.parsed.servers

        return response
