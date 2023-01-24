from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Tuple, Union

from binarylane.api.vpcs.put_v2_vpcs_vpc_id import sync_detailed
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.route_entry_request import RouteEntryRequest
from binarylane.models.update_vpc_request import UpdateVpcRequest
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.models.vpc_response import VpcResponse
from binarylane.types import Unset

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import ListAttribute, Mapping
from binarylane.console.runners.command import CommandRunner


class CommandRequest:
    vpc_id: int
    json_body: UpdateVpcRequest

    def __init__(self, vpc_id: int, json_body: UpdateVpcRequest) -> None:
        self.vpc_id = vpc_id
        self.json_body = json_body


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "update"

    @property
    def description(self) -> str:
        return """Update an Existing VPC"""

    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/Vpcs/paths/~1v2~1vpcs~1%7Bvpc_id%7D/put"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        mapping.add_primitive(
            "vpc_id",
            int,
            required=True,
            option_name=None,
            description="""The target vpc id.""",
        )

        json_body = mapping.add_json_body(UpdateVpcRequest)

        json_body.add_primitive(
            "name",
            str,
            option_name="name",
            required=True,
            description="""A name to help identify this VPC.""",
        )

        json_body_route_entry_request = json_body.add(
            ListAttribute(
                "route_entries",
                RouteEntryRequest,
                option_name="route-entries",
                description="""The route entries that control how network traffic is directed through the VPC environment.""",
                required=False,
            )
        )

        json_body_route_entry_request.add_primitive(
            "router",
            str,
            option_name="router",
            required=True,
            description="""The server that will receive traffic sent to the destination property in this VPC.""",
        )

        json_body_route_entry_request.add_primitive(
            "destination",
            str,
            option_name="destination",
            required=True,
            description="""The destination address for this route entry. This may be in CIDR format.""",
        )

        json_body_route_entry_request.add_primitive(
            "description",
            Union[Unset, None, str],
            option_name="description",
            required=False,
            description="""An optional description for the route.""",
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
