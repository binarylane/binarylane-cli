from __future__ import annotations

import datetime
from http import HTTPStatus
from typing import TYPE_CHECKING, Dict, List, Optional, Tuple, Union

from binarylane.api.sample_sets.get_v2_samplesets_server_id import sync_detailed
from binarylane.models.data_interval import DataInterval
from binarylane.models.links import Links
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.sample_sets_response import SampleSetsResponse
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import UNSET, Unset

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import Mapping
from binarylane.console.runners.list import ListRunner


class CommandRequest:
    server_id: int
    data_interval: Union[Unset, None, DataInterval] = UNSET
    start: Union[Unset, None, datetime.datetime] = UNSET
    end: Union[Unset, None, datetime.datetime] = UNSET

    def __init__(self, server_id: int) -> None:
        self.server_id = server_id


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
            "period": """The period when this sample set was collected.""",
            "average": """The average values of the samples collected during this period.""",
            "maximum_memory_megabytes": """The maximum memory used in MB at any point during this collection period.""",
            "maximum_storage_gigabytes": """The maximum storage used in GB at any point during this collection period.""",
        }

    @property
    def name(self) -> str:
        return "list"

    @property
    def description(self) -> str:
        return """Fetch all of the Performance and Usage Data Sample Sets for a Server"""

    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/SampleSets/paths/~1v2~1samplesets~1%7Bserver_id%7D/get"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        mapping.add_primitive(
            "server_id",
            int,
            required=True,
            option_name=None,
            description="""The target server id.""",
        )

        mapping.add_primitive(
            "data_interval",
            Union[Unset, None, DataInterval],
            required=False,
            option_name="data-interval",
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
        mapping.add_primitive(
            "start",
            Union[Unset, None, datetime.datetime],
            required=False,
            option_name="start",
            description="""The start of the window of samples to retrieve, ISO8601 format (eg 2022-12-30T22:50:00Z). Defaults to 1 week before end for intervals larger than 5 minutes, or 1 day for 5 minute intervals.""",
        )
        mapping.add_primitive(
            "end",
            Union[Unset, None, datetime.datetime],
            required=False,
            option_name="end",
            description="""The start of the window of samples to retrieve, ISO8601 format (eg 2022-12-30T22:50:00Z). Defaults to 1 week or 1 day after start date depending on the selected data interval (or the current time if start is not provided). Can't be more than 1 year from start.""",
        )
        return mapping

    @property
    def ok_response_type(self) -> type:
        return SampleSetsResponse

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[None, ProblemDetails, SampleSetsResponse, ValidationProblemDetails]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.OK: SampleSetsResponse
        # HTTPStatus.BAD_REQUEST: ValidationProblemDetails
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page = 0
        per_page = 25
        has_next = True
        response: Optional[SampleSetsResponse] = None

        while has_next:
            page += 1
            page_response = sync_detailed(
                server_id=request.server_id,
                client=client,
                data_interval=request.data_interval,
                start=request.start,
                end=request.end,
                page=page,
                per_page=per_page,
            )

            status_code = page_response.status_code
            if status_code != 200:
                return status_code, page_response.parsed

            assert isinstance(page_response.parsed, SampleSetsResponse)
            has_next = isinstance(page_response.parsed.links, Links) and isinstance(
                page_response.parsed.links.pages.next_, str
            )
            if not response:
                response = page_response.parsed
            else:
                response.sample_sets += page_response.parsed.sample_sets

        return status_code, response
