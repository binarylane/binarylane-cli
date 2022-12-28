from typing import Union

from ...client.api.server.server_kernel_list import sync
from ...client.client import Client
from ...client.types import Unset
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server_kernel_list"

    @property
    def description(self):
        return """List all Available Kernels for a Server"""

    def configure(self, parser):
        """Add arguments for server_kernel_list"""
        parser.cli_argument(
            "server_id",
            description="""The target server id.""",
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
        server_id: int,
        client: Client,
        page: Union[Unset, None, int] = 1,
        per_page: Union[Unset, None, int] = 20,
    ):
        return sync(
            server_id=server_id,
            client=client,
            page=page,
            per_page=per_page,
        )
