from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Tuple, Union

from binarylane.api.vpcs.post_v2_vpcs import sync_detailed
from binarylane.models.create_vpc_request import CreateVpcRequest
from binarylane.models.route_entry_request import RouteEntryRequest
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.models.vpc_response import VpcResponse
from binarylane.types import Unset

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import ListAttribute, Mapping
from binarylane.console.runners.command import CommandRunner


class CommandRequest:
    json_body: CreateVpcRequest

    def __init__(self, json_body: CreateVpcRequest) -> None:
        self.json_body = json_body


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "create"

    @property
    def description(self) -> str:
        return """Create a New VPC"""

    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/Vpcs/paths/~1v2~1vpcs/post"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        json_body = mapping.add_json_body(CreateVpcRequest)

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

        json_body.add_primitive(
            "ip_range",
            Union[Unset, None, str],
            option_name="ip-range",
            required=False,
            description="""A private address range that you select during creation, such as the default value of 10.240.0.0/16. Because the virtual network is dedicated to your use, you may use whatever IP address range you like.""",
        )

        return mapping

    @property
    def ok_response_type(self) -> type:
        return VpcResponse

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[None, ValidationProblemDetails, VpcResponse]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.OK: VpcResponse
        # HTTPStatus.BAD_REQUEST: ValidationProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            client=client,
            json_body=request.json_body,
        )
        return page_response.status_code, page_response.parsed
