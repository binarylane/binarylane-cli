from __future__ import annotations

from http import HTTPStatus
from typing import List, Tuple, Union

from binarylane.api.vpc.vpc_patch import sync_detailed
from binarylane.client import Client
from binarylane.models.patch_vpc_request import PatchVpcRequest
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.route_entry_request import RouteEntryRequest
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.models.vpc_response import VpcResponse
from binarylane.types import UNSET, Unset

from binarylane.console.parsers import CommandParser
from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "patch"

    @property
    def description(self) -> str:
        return """Update an Existing VPC"""

    def configure(self, parser: CommandParser) -> None:
        """Add arguments for vpc_patch"""
        parser.cli_argument(
            "vpc_id",
            int,
            description="""The target vpc id.""",
        )

        parser.cli_argument(
            "--name",
            Union[Unset, None, str],
            dest="name",
            required=False,
            description=""">A name to help identify this VPC. Submit null to leave unaltered.""",
        )

        parser.cli_argument(
            "--route-entries",
            Union[Unset, None, List[RouteEntryRequest]],
            dest="route_entries",
            required=False,
            description="""Submit null to leave unaltered, submit an empty list to clear all route entries. It is not possible to PATCH individual route entries, to alter a route entry submit the entire list of route entries you wish to save.""",
        )

    @property
    def ok_response_type(self) -> type:
        return VpcResponse

    def request(
        self,
        vpc_id: int,
        client: Client,
        name: Union[Unset, None, str] = UNSET,
        route_entries: Union[Unset, None, List[RouteEntryRequest]] = UNSET,
    ) -> Tuple[HTTPStatus, Union[None, ProblemDetails, ValidationProblemDetails, VpcResponse]]:

        # HTTPStatus.OK: VpcResponse
        # HTTPStatus.BAD_REQUEST: ValidationProblemDetails
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            vpc_id=vpc_id,
            client=client,
            json_body=PatchVpcRequest(
                name=name,
                route_entries=route_entries,
            ),
        )
        return page_response.status_code, page_response.parsed
