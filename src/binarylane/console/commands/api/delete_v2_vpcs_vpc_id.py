from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Tuple, Union

from binarylane.api.vpcs.delete_v2_vpcs_vpc_id import sync_detailed
from binarylane.models.problem_details import ProblemDetails

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import Mapping
from binarylane.console.runners.command import CommandRunner


class CommandRequest:
    vpc_id: int

    def __init__(self, vpc_id: int) -> None:
        self.vpc_id = vpc_id


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "delete"

    @property
    def description(self) -> str:
        return """Delete an Existing VPC"""

    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/Vpcs/paths/~1v2~1vpcs~1%7Bvpc_id%7D/delete"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        mapping.add_primitive(
            "vpc_id",
            int,
            required=True,
            option_name=None,
            description="""The target vpc id.""",
        )

        return mapping

    @property
    def ok_response_type(self) -> type:
        return type(None)

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[None, ProblemDetails]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.NO_CONTENT: Any
        # HTTPStatus.FORBIDDEN: ProblemDetails
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            vpc_id=request.vpc_id,
            client=client,
        )
        return page_response.status_code, page_response.parsed
