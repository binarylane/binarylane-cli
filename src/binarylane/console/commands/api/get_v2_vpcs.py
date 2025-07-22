from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Tuple, Union

from binarylane.api.vpcs.get_v2_vpcs import sync_detailed
from binarylane.console.util import create_client
from binarylane.models.links import Links
from binarylane.models.vpcs_response import VpcsResponse

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import Mapping
from binarylane.console.runners.list import ListRunner


class CommandRequest:
    pass


class Command(ListRunner):
    def response(self, status_code: int, received: Any) -> None:
        if not isinstance(received, VpcsResponse):
            return super().response(status_code, received)

        return self._printer.print(received, self._format)

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

    def lookup(self, ref: str) -> Optional[int]:
        status_code, received = self.request(create_client(self._context), CommandRequest())
        if status_code != 200:
            super().response(status_code, received)

        assert isinstance(received, VpcsResponse)
        for item in received.vpcs:
            if item.name == ref:
                return item.id
        else:
            return None

    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/Vpcs/paths/~1v2~1vpcs/get"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)
        return mapping

    @property
    def ok_response_type(self) -> type:
        return VpcsResponse

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[None, VpcsResponse]]:
        assert isinstance(request, CommandRequest)

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
