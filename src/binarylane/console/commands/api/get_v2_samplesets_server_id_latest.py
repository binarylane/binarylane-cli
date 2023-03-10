from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Tuple, Union

from binarylane.api.sample_sets.get_v2_samplesets_server_id_latest import sync_detailed
from binarylane.models.data_interval import DataInterval
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.sample_set_response import SampleSetResponse
from binarylane.types import UNSET, Unset

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import Mapping
from binarylane.console.runners.command import CommandRunner


class CommandRequest:
    server_id: int
    data_interval: Union[Unset, None, DataInterval] = UNSET

    def __init__(self, server_id: int) -> None:
        self.server_id = server_id


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "get"

    @property
    def description(self) -> str:
        return """Fetch the Latest Performance and Usage Data Sample Set for a Server"""

    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/SampleSets/paths/~1v2~1samplesets~1%7Bserver_id%7D~1latest/get"

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
        return mapping

    @property
    def ok_response_type(self) -> type:
        return SampleSetResponse

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[None, ProblemDetails, SampleSetResponse]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.OK: SampleSetResponse
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            server_id=request.server_id,
            client=client,
            data_interval=request.data_interval,
        )
        return page_response.status_code, page_response.parsed
