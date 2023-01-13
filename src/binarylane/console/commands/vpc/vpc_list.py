from __future__ import annotations

from http import HTTPStatus
from typing import Dict, List, Optional, Tuple, Union

from binarylane.api.vpc.vpc_list import sync_detailed
from binarylane.client import Client
from binarylane.models.links import Links
from binarylane.models.vpcs_response import VpcsResponse

from binarylane.console.parsers import CommandParser
from binarylane.console.runners import ListRunner


class Command(ListRunner):
    @property
    def default_format(self) -> List[str]:
        return [
            "id",
            "name",
            "ip_range",
        ]

    @property
    def fields(self) -> Dict[str, str]:
        return {
            "id": """The ID of this VPC.""",
            "name": """The name of this VPC.""",
            "ip_range": """The IPv4 range for this VPC in CIDR format.""",
            "route_entries": """The route entries that control how network traffic is directed through the VPC environment.""",
        }

    @property
    def name(self) -> str:
        return "list"

    @property
    def description(self) -> str:
        return """List All Existing VPCs"""

    def configure(self, parser: CommandParser) -> None:
        """Add arguments for vpc_list"""

    @property
    def ok_response_type(self) -> type:
        return VpcsResponse

    def request(
        self,
        client: Client,
    ) -> Tuple[HTTPStatus, Union[None, VpcsResponse]]:

        # HTTPStatus.OK: VpcsResponse
        # HTTPStatus.UNAUTHORIZED: Any
        page = 0
        per_page = 25
        has_next = True
        response: Optional[VpcsResponse] = None

        while has_next:
            page += 1
            page_response = sync_detailed(
                client=client,
                page=page,
                per_page=per_page,
            )

            status_code = page_response.status_code
            if status_code != 200:
                return status_code, page_response.parsed

            assert isinstance(page_response.parsed, VpcsResponse)
            has_next = isinstance(page_response.parsed.links, Links) and isinstance(
                page_response.parsed.links.pages.next_, str
            )
            if not response:
                response = page_response.parsed
            else:
                response.vpcs += page_response.parsed.vpcs

        return status_code, response
