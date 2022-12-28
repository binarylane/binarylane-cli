from typing import Union

from ...client.api.server.server_metrics_get import sync
from ...client.client import Client
from ...client.models.data_interval import DataInterval
from ...client.types import UNSET, Unset
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server_metrics_get"

    @property
    def description(self):
        return """Fetch the Latest Performance and Usage Data Sample Set for a Server"""

    def configure(self, parser):
        """Add arguments for server_metrics_get"""
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

    def request(
        self,
        server_id: int,
        client: Client,
        data_interval: Union[Unset, None, DataInterval] = UNSET,
    ):
        return sync(
            server_id=server_id,
            client=client,
            data_interval=data_interval,
        )
