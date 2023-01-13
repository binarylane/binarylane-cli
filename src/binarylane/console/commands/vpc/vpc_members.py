from __future__ import annotations

from http import HTTPStatus
from typing import Dict, List, Optional, Tuple, Union

from binarylane.api.vpc.vpc_members import sync_detailed
from binarylane.client import Client
from binarylane.models.links import Links
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.resource_type import ResourceType
from binarylane.models.vpc_members_response import VpcMembersResponse
from binarylane.types import UNSET, Unset

from binarylane.console.parsers import CommandParser
from binarylane.console.runners import ListRunner


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

    def configure(self, parser: CommandParser) -> None:
        """Add arguments for vpc_members"""
        parser.cli_argument(
            "vpc_id",
            int,
            description="""The target vpc id.""",
        )

        parser.cli_argument(
            "--resource-type",
            Union[Unset, None, ResourceType],
            dest="resource_type",
            required=False,
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

    @property
    def ok_response_type(self) -> type:
        return VpcMembersResponse

    def request(
        self,
        vpc_id: int,
        client: Client,
        resource_type: Union[Unset, None, ResourceType] = UNSET,
    ) -> Tuple[HTTPStatus, Union[None, ProblemDetails, VpcMembersResponse]]:

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
                vpc_id=vpc_id,
                client=client,
                resource_type=resource_type,
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
