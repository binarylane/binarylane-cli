from typing import Any, Union

from ...client.api.server.server_metrics_get import sync_detailed
from ...client.client import Client
from ...client.models.data_interval import DataInterval
from ...client.models.problem_details import ProblemDetails
from ...client.models.sample_set_response import SampleSetResponse
from ...client.types import UNSET, Unset
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "get"

    @property
    def description(self):
        return """Fetch the Latest Performance and Usage Data Sample Set for a Server"""

    def configure(self, parser):
        """Add arguments for server_metrics_get"""
        parser.cli_argument(
            "server_id",
            type=int,
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
    ) -> Union[Any, ProblemDetails, SampleSetResponse]:

        page_response = sync_detailed(
            server_id=server_id,
            client=client,
            data_interval=data_interval,
        )
        return page_response.status_code, page_response.parsed
