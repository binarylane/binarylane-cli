from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Tuple, Union

from binarylane.api.vpcs.get_v2_vpcs_vpc_id import sync_detailed
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.vpc_response import VpcResponse

if TYPE_CHECKING:
    from binarylane.client import Client

import binarylane.console.commands.api.get_v2_vpcs as api_get_v2_vpcs
from binarylane.console.parser import Mapping, PrimitiveAttribute
from binarylane.console.runners.command import CommandRunner


class CommandRequest:
    vpc_id: int

    def __init__(self, vpc_id: int) -> None:
        self.vpc_id = vpc_id


class Command(CommandRunner):
    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/Vpcs/paths/~1v2~1vpcs~1%7Bvpc_id%7D/get"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        def lookup_vpc_id(ref: str) -> Union[None, int]:
            return api_get_v2_vpcs.Command(self._context).lookup(ref)

        mapping.add(
            PrimitiveAttribute(
                "vpc_id",
                int,
                required=True,
                option_name=None,
                metavar="vpc",
                description="""The target vpc id or name.""",
                lookup=lookup_vpc_id,
            )
        )

        return mapping

    @property
    def ok_response_type(self) -> type:
        return VpcResponse

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[None, ProblemDetails, VpcResponse]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.OK: VpcResponse
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            vpc_id=request.vpc_id,
            client=client,
        )
        return page_response.status_code, page_response.parsed
