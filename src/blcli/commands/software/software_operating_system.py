from typing import Union

from ...client.api.software.software_operating_system import sync
from ...client.client import Client
from ...client.types import Unset
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "software_operating-system"

    @property
    def description(self):
        return """List All Available Software for an Existing Operating System"""

    def configure(self, parser):
        """Add arguments for software_operating-system"""
        parser.cli_argument(
            "operating_system_id_or_slug",
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
        operating_system_id_or_slug: str,
        client: Client,
        page: Union[Unset, None, int] = 1,
        per_page: Union[Unset, None, int] = 20,
    ):
        return sync(
            operating_system_id_or_slug=operating_system_id_or_slug,
            client=client,
            page=page,
            per_page=per_page,
        )
