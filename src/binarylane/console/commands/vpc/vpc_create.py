from __future__ import annotations

from typing import Any, List, Type, Union

from binarylane.api.vpc.vpc_create import sync_detailed
from binarylane.client import Client
from binarylane.models.create_vpc_request import CreateVpcRequest
from binarylane.models.route_entry_request import RouteEntryRequest
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.models.vpc_response import VpcResponse
from binarylane.types import UNSET, Unset

from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "create"

    @property
    def description(self):
        return """Create a New VPC"""

    def configure(self, parser):
        """Add arguments for vpc_create"""

        parser.cli_argument(
            "--name",
            dest="name",
            type=str,
            required=True,
            description="""A name to help identify this VPC.""",
        )

        parser.cli_argument(
            "--route-entries",
            dest="route_entries",
            type=Union[Unset, None, List["RouteEntryRequest"]],
            required=False,
            description="""The route entries that control how network traffic is directed through the VPC environment.""",
        )

        parser.cli_argument(
            "--ip-range",
            dest="ip_range",
            type=Union[Unset, None, str],
            required=False,
            description="""A private address range that you select during creation, such as the default value of 10.240.0.0/16. Because the virtual network is dedicated to your use, you may use whatever IP address range you like.""",
        )

    @property
    def ok_response_type(self) -> Type:
        return VpcResponse

    def request(
        self,
        client: Client,
        name: str,
        route_entries: Union[Unset, None, List["RouteEntryRequest"]] = UNSET,
        ip_range: Union[Unset, None, str] = UNSET,
    ) -> Union[Any, ValidationProblemDetails, VpcResponse]:

        page_response = sync_detailed(
            client=client,
            json_body=CreateVpcRequest(
                name=name,
                route_entries=route_entries,
                ip_range=ip_range,
            ),
        )
        return page_response.status_code, page_response.parsed
