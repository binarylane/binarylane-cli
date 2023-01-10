from __future__ import annotations

import datetime
from typing import Any, Dict, List, Type, Union

from binarylane.api.server.server_metrics_list import sync_detailed
from binarylane.client import Client
from binarylane.models.data_interval import DataInterval
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.sample_sets_response import SampleSetsResponse
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import UNSET, Unset

from binarylane.console.runners import ListRunner


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
            int,
            description="""The target server id.""",
        )

        parser.cli_argument(
            "--data-interval",
            Union[Unset, None, DataInterval],
            dest="data_interval",
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
            Union[Unset, None, datetime.datetime],
            dest="start",
            required=False,
            description="""The start of the window of samples to retrieve, ISO8601 format (eg 2022-12-30T22:50:00Z). Defaults to 1 week before end for intervals larger than 5 minutes, or 1 day for 5 minute intervals.""",
        )
        parser.cli_argument(
            "--end",
            Union[Unset, None, datetime.datetime],
            dest="end",
            required=False,
            description="""The start of the window of samples to retrieve, ISO8601 format (eg 2022-12-30T22:50:00Z). Defaults to 1 week or 1 day after start date depending on the selected data interval (or the current time if start is not provided). Can't be more than 1 year from start.""",
        )

    @property
    def ok_response_type(self) -> Type:
        return SampleSetsResponse

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

            status_code = page_response.status_code
            if status_code != 200:
                response = page_response.parsed
                break

            has_next = page_response.parsed.links and page_response.parsed.links.pages.next_
            if not response:
                response = page_response.parsed
            else:
                response.sample_sets += page_response.parsed.sample_sets

        return status_code, response
