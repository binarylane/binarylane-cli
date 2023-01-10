from __future__ import annotations

from typing import Any, Type, Union

from binarylane.api.server_action.server_action_change_vpc_ipv4 import sync_detailed
from binarylane.client import Client
from binarylane.models.action_response import ActionResponse
from binarylane.models.change_vpc_ipv_4 import ChangeVpcIpv4
from binarylane.models.change_vpc_ipv_4_type import ChangeVpcIpv4Type
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails

from binarylane.console.runners import ActionRunner


class Command(ActionRunner):
    @property
    def name(self):
        return "change-vpc-ipv4"

    @property
    def description(self):
        return """Change the IPv4 Address for a Server in a VPC"""

    def configure(self, parser):
        """Add arguments for server-action_change-vpc-ipv4"""
        parser.cli_argument(
            "server_id",
            int,
            description="""The ID of the server on which the action should be performed.""",
        )

        parser.cli_argument(
            "--type",
            ChangeVpcIpv4Type,
            dest="type",
            required=True,
            description="""None""",
        )

        parser.cli_argument(
            "--current-ipv4-address",
            str,
            dest="current_ipv4_address",
            required=True,
            description="""The existing Ipv4 address for the private VPC network adapter you wish to change.""",
        )

        parser.cli_argument(
            "--new-ipv4-address",
            str,
            dest="new_ipv4_address",
            required=True,
            description="""The new Ipv4 address for the private VPC network adapter.""",
        )

    @property
    def ok_response_type(self) -> Type:
        return ActionResponse

    def request(
        self,
        server_id: int,
        client: Client,
        type: ChangeVpcIpv4Type,
        current_ipv4_address: str,
        new_ipv4_address: str,
    ) -> Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]:

        page_response = sync_detailed(
            server_id=server_id,
            client=client,
            json_body=ChangeVpcIpv4(
                type=type,
                current_ipv4_address=current_ipv4_address,
                new_ipv4_address=new_ipv4_address,
            ),
        )
        return page_response.status_code, page_response.parsed
