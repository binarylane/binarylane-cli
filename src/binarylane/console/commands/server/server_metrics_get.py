from __future__ import annotations

from http import HTTPStatus
from typing import Tuple, Union

from binarylane.api.server.server_metrics_get import sync_detailed
from binarylane.client import Client
from binarylane.models.data_interval import DataInterval
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.sample_set_response import SampleSetResponse
from binarylane.types import UNSET, Unset

from binarylane.console.parsers import CommandParser
from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "get"

    @property
    def description(self) -> str:
        return """Fetch the Latest Performance and Usage Data Sample Set for a Server"""

    def configure(self, parser: CommandParser) -> None:
        """Add arguments for server_metrics_get"""
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

    @property
    def ok_response_type(self) -> type:
        return SampleSetResponse

    def request(
        self,
        server_id: int,
        client: Client,
        data_interval: Union[Unset, None, DataInterval] = UNSET,
    ) -> Tuple[HTTPStatus, Union[None, ProblemDetails, SampleSetResponse]]:

        # HTTPStatus.OK: SampleSetResponse
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            server_id=server_id,
            client=client,
            data_interval=data_interval,
        )
        return page_response.status_code, page_response.parsed
