import datetime
from typing import Union

from ...client.api.server.server_metrics_list import sync
from ...client.client import Client
from ...client.models.data_interval import DataInterval
from ...client.types import UNSET, Unset
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server_metrics_list"

    @property
    def description(self):
        return """Fetch all of the Performance and Usage Data Sample Sets for a Server"""

    def configure(self, parser):
        """Add arguments for server_metrics_list"""
        parser.cli_argument(
            "server_id",
            description="""The target server id.""",
        )

        parser.cli_argument(
            "--data-interval",
            dest="data_interval",
            type=Union[Unset, None, DataInterval],
            required=False,
            description="""
| Value | Description |
| ----- | ----------- |
| five-minute | 5 Minutes |
| half-hour | 30 Minutes |
| four-hour | 4 Hours |
| day | 1 Day |
| week | 7 Days |
| month | 1 Month |

""",
        )
        parser.cli_argument(
            "--start",
            dest="start",
            type=Union[Unset, None, datetime.datetime],
            required=False,
            description="""None""",
        )
        parser.cli_argument(
            "--end",
            dest="end",
            type=Union[Unset, None, datetime.datetime],
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
        server_id: int,
        client: Client,
        data_interval: Union[Unset, None, DataInterval] = UNSET,
        start: Union[Unset, None, datetime.datetime] = UNSET,
        end: Union[Unset, None, datetime.datetime] = UNSET,
        page: Union[Unset, None, int] = 1,
        per_page: Union[Unset, None, int] = 20,
    ):
        return sync(
            server_id=server_id,
            client=client,
            data_interval=data_interval,
            start=start,
            end=end,
            page=page,
            per_page=per_page,
        )
