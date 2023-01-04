import datetime
from typing import Any, Dict, List, Union

from ...client.api.server.server_metrics_list import sync_detailed
from ...client.client import Client
from ...client.models.data_interval import DataInterval
from ...client.models.problem_details import ProblemDetails
from ...client.models.sample_sets_response import SampleSetsResponse
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...client.types import UNSET, Unset
from ...runners import ListRunner


class Command(ListRunner):
    @property
    def default_format(self) -> List[str]:
        return [
            "server_id",
            "maximum_memory_megabytes",
            "maximum_storage_gigabytes",
        ]

    @property
    def fields(self) -> Dict[str, str]:
        return {
            "server_id": """The ID of the server that this sample set refers to.""",
            "period": """""",
            "average": """""",
            "maximum_memory_megabytes": """The maximum memory used in MB at any point during this collection period.""",
            "maximum_storage_gigabytes": """The maximum storage used in GB at any point during this collection period.""",
        }

    @property
    def name(self):
        return "list"

    @property
    def description(self):
        return """Fetch all of the Performance and Usage Data Sample Sets for a Server"""

    def configure(self, parser):
        """Add arguments for server_metrics_list"""
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

    def request(
        self,
        server_id: int,
        client: Client,
        data_interval: Union[Unset, None, DataInterval] = UNSET,
        start: Union[Unset, None, datetime.datetime] = UNSET,
        end: Union[Unset, None, datetime.datetime] = UNSET,
    ) -> Union[Any, ProblemDetails, SampleSetsResponse, ValidationProblemDetails]:

        page = 0
        per_page = 25
        has_next = True
        response: SampleSetsResponse = None

        while has_next:
            page += 1
            page_response = sync_detailed(
                server_id=server_id,
                client=client,
                data_interval=data_interval,
                start=start,
                end=end,
                page=page,
                per_page=per_page,
            )

            if page_response.status_code != 200:
                return page_response.parsed

            has_next = page_response.parsed.links and page_response.parsed.links.pages.next_
            if not response:
                response = page_response.parsed
            else:
                response.sample_sets += page_response.parsed.sample_sets

        return response
