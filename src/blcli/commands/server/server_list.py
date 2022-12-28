from typing import Union

from ...client.api.server.server_list import sync
from ...client.client import Client
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
        parser.cli_argument(
            "--page",
            dest="page",
            type=Union[Unset, None, int],
            required=False,
            description="""The selected page. Page numbering starts at 1""",
        )
        parser.cli_argument(
            "--per-page",
            dest="per_page",
            type=Union[Unset, None, int],
            required=False,
            description="""The number of results to show per page.""",
        )

    def request(
        self,
        client: Client,
        tag_name: Union[Unset, None, str] = UNSET,
        page: Union[Unset, None, int] = 1,
        per_page: Union[Unset, None, int] = 20,
    ):
        return sync(
            client=client,
            tag_name=tag_name,
            page=page,
            per_page=per_page,
        )
