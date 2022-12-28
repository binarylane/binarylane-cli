from typing import Any, List, Union

from ...client.api.vpc.vpc_patch import sync_detailed
from ...client.client import Client
from ...client.models.patch_vpc_request import PatchVpcRequest
from ...client.models.problem_details import ProblemDetails
from ...client.models.route_entry_request import RouteEntryRequest
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...client.models.vpc_response import VpcResponse
from ...client.types import UNSET, Unset
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "vpc_patch"

    @property
    def description(self):
        return """Update an Existing VPC"""

    def configure(self, parser):
        """Add arguments for vpc_patch"""
        parser.cli_argument(
            "vpc_id",
            description="""The target vpc id.""",
        )

        parser.cli_argument(
            "--name",
            dest="name",
            type=Union[Unset, None, str],
            required=False,
            description=""">A name to help identify this VPC. Submit null to leave unaltered.""",
        )

        parser.cli_argument(
            "--route-entries",
            dest="route_entries",
            type=Union[Unset, None, List[RouteEntryRequest]],
            required=False,
            description="""Submit null to leave unaltered, submit an empty list to clear all route entries. It is not possible to PATCH individual route entries, to alter a route entry submit the entire list of route entries you wish to save.""",
        )

    def request(
        self,
        vpc_id: int,
        client: Client,
        name: Union[Unset, None, str] = UNSET,
        route_entries: Union[Unset, None, List[RouteEntryRequest]] = UNSET,
    ) -> Union[Any, ProblemDetails, ValidationProblemDetails, VpcResponse]:

        return sync_detailed(
            vpc_id=vpc_id,
            client=client,
            json_body=PatchVpcRequest(
                name=name,
                route_entries=route_entries,
            ),
        ).parsed
