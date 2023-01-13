from __future__ import annotations

from http import HTTPStatus
from typing import List, Tuple, Union

from binarylane.api.vpc.vpc_create import sync_detailed
from binarylane.client import Client
from binarylane.models.create_vpc_request import CreateVpcRequest
from binarylane.models.route_entry_request import RouteEntryRequest
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.models.vpc_response import VpcResponse
from binarylane.types import UNSET, Unset

from binarylane.console.parsers import CommandParser
from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "create"

    @property
    def description(self) -> str:
        return """Create a New VPC"""

    def configure(self, parser: CommandParser) -> None:
        """Add arguments for vpc_create"""

        parser.cli_argument(
            "--name",
            str,
            dest="name",
            required=True,
            description="""A name to help identify this VPC.""",
        )

        parser.cli_argument(
            "--route-entries",
            Union[Unset, None, List[RouteEntryRequest]],
            dest="route_entries",
            required=False,
            description="""The route entries that control how network traffic is directed through the VPC environment.""",
        )

        parser.cli_argument(
            "--ip-range",
            Union[Unset, None, str],
            dest="ip_range",
            required=False,
            description="""A private address range that you select during creation, such as the default value of 10.240.0.0/16. Because the virtual network is dedicated to your use, you may use whatever IP address range you like.""",
        )

    @property
    def ok_response_type(self) -> type:
        return VpcResponse

    def request(
        self,
        client: Client,
        name: str,
        route_entries: Union[Unset, None, List[RouteEntryRequest]] = UNSET,
        ip_range: Union[Unset, None, str] = UNSET,
    ) -> Tuple[HTTPStatus, Union[None, ValidationProblemDetails, VpcResponse]]:

        # HTTPStatus.OK: VpcResponse
        # HTTPStatus.BAD_REQUEST: ValidationProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            client=client,
            json_body=CreateVpcRequest(
                name=name,
                route_entries=route_entries,
                ip_range=ip_range,
            ),
        )
        return page_response.status_code, page_response.parsed
