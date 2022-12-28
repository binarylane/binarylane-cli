from typing import Union

from ...client.api.size.size_list import sync
from ...client.client import Client
from ...client.types import UNSET, Unset
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "size_list"

    @property
    def description(self):
        return """List All Available Sizes"""

    def configure(self, parser):
        """Add arguments for size_list"""

        parser.cli_argument(
            "--server-id",
            dest="server_id",
            type=Union[Unset, None, int],
            required=False,
            description="""None""",
        )
        parser.cli_argument(
            "--image",
            dest="image",
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
        server_id: Union[Unset, None, int] = UNSET,
        image: Union[Unset, None, str] = UNSET,
        page: Union[Unset, None, int] = 1,
        per_page: Union[Unset, None, int] = 20,
    ):
        return sync(
            client=client,
            server_id=server_id,
            image=image,
            page=page,
            per_page=per_page,
        )
