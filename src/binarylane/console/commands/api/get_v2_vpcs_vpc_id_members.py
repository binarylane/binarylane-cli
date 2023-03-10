from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Dict, List, Optional, Tuple, Union

from binarylane.api.vpcs.get_v2_vpcs_vpc_id_members import sync_detailed
from binarylane.models.links import Links
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.resource_type import ResourceType
from binarylane.models.vpc_members_response import VpcMembersResponse
from binarylane.types import UNSET, Unset

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import Mapping
from binarylane.console.runners.list import ListRunner


class CommandRequest:
    vpc_id: int
    resource_type: Union[Unset, None, ResourceType] = UNSET

    def __init__(self, vpc_id: int) -> None:
        self.vpc_id = vpc_id


class Command(ListRunner):
    @property
    def default_format(self) -> List[str]:
        return [
            "name",
            "resource_type",
            "resource_id",
        ]

    @property
    def fields(self) -> Dict[str, str]:
        return {
            "name": """The name of this VPC member.""",
            "resource_type": """
| Value | Description |
| ----- | ----------- |
| server | Server |
| load-balancer | Load Balancer |
| ssh-key | SSH Key |
| vpc | Virtual Private Network |
| image | Backup or Operating System Image |
| registered-domain-name | Registered Domain Name |

""",
            "resource_id": """The resource ID of this VPC member.""",
            "created_at": """The date and time in ISO8601 format of this resource's initial creation.""",
        }

    @property
    def name(self) -> str:
        return "members"

    @property
    def description(self) -> str:
        return """List All Members of an Existing VPC"""

    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/Vpcs/paths/~1v2~1vpcs~1%7Bvpc_id%7D~1members/get"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        mapping.add_primitive(
            "vpc_id",
            int,
            required=True,
            option_name=None,
            description="""The target vpc id.""",
        )

        mapping.add_primitive(
            "resource_type",
            Union[Unset, None, ResourceType],
            required=False,
            option_name="resource-type",
            description="""
| Value | Description |
| ----- | ----------- |
| server | Server |
| load-balancer | Load Balancer |
| ssh-key | SSH Key |
| vpc | Virtual Private Network |
| image | Backup or Operating System Image |
| registered-domain-name | Registered Domain Name |

""",
        )
        return mapping

    @property
    def ok_response_type(self) -> type:
        return VpcMembersResponse

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[None, ProblemDetails, VpcMembersResponse]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.OK: VpcMembersResponse
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page = 0
        per_page = 25
        has_next = True
        response: Optional[VpcMembersResponse] = None

        while has_next:
            page += 1
            page_response = sync_detailed(
                vpc_id=request.vpc_id,
                client=client,
                resource_type=request.resource_type,
                page=page,
                per_page=per_page,
            )

            status_code = page_response.status_code
            if status_code != 200:
                return status_code, page_response.parsed

            assert isinstance(page_response.parsed, VpcMembersResponse)
            has_next = isinstance(page_response.parsed.links, Links) and isinstance(
                page_response.parsed.links.pages.next_, str
            )
            if not response:
                response = page_response.parsed
            else:
                response.members += page_response.parsed.members

        return status_code, response
