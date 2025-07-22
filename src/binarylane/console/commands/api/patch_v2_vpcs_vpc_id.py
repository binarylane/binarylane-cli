from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Tuple, Union

from binarylane.api.vpcs.patch_v2_vpcs_vpc_id import sync_detailed
from binarylane.models.patch_vpc_request import PatchVpcRequest
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.route_entry_request import RouteEntryRequest
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.models.vpc_response import VpcResponse
from binarylane.types import Unset

if TYPE_CHECKING:
    from binarylane.client import Client

import binarylane.console.commands.api.get_v2_vpcs as api_get_v2_vpcs
from binarylane.console.parser import ListAttribute, Mapping, PrimitiveAttribute
from binarylane.console.runners.command import CommandRunner


class CommandRequest:
    vpc_id: int
    json_body: PatchVpcRequest

    def __init__(self, vpc_id: int, json_body: PatchVpcRequest) -> None:
        self.vpc_id = vpc_id
        self.json_body = json_body


class Command(CommandRunner):
    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/Vpcs/paths/~1v2~1vpcs~1%7Bvpc_id%7D/patch"

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

        json_body = mapping.add_json_body(PatchVpcRequest)

        json_body.add(
            PrimitiveAttribute(
                "name",
                Union[Unset, None, str],
                required=False,
                option_name="name",
                description=""">A name to help identify this VPC. Submit null to leave unaltered.""",
            )
        )

        json_body_route_entry_request = json_body.add(
            ListAttribute(
                "route_entries",
                RouteEntryRequest,
                required=False,
                option_name="route-entries",
                description="""Submit null to leave unaltered, submit an empty list to clear all route entries. It is not possible to PATCH individual route entries, to alter a route entry submit the entire list of route entries you wish to save.""",
            )
        )

        json_body_route_entry_request.add(
            PrimitiveAttribute(
                "router",
                str,
                required=True,
                option_name="router",
                description="""The server that will receive traffic sent to the destination property in this VPC.""",
            )
        )

        json_body_route_entry_request.add(
            PrimitiveAttribute(
                "destination",
                str,
                required=True,
                option_name="destination",
                description="""The destination address for this route entry. This may be in CIDR format.""",
            )
        )

        json_body_route_entry_request.add(
            PrimitiveAttribute(
                "description",
                Union[Unset, None, str],
                required=False,
                option_name="description",
                description="""An optional description for the route.""",
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
    ) -> Tuple[HTTPStatus, Union[None, ProblemDetails, ValidationProblemDetails, VpcResponse]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.OK: VpcResponse
        # HTTPStatus.BAD_REQUEST: ValidationProblemDetails
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            vpc_id=request.vpc_id,
            client=client,
            json_body=request.json_body,
        )
        return page_response.status_code, page_response.parsed
