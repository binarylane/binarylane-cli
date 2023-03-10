from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Any, Tuple, Union

from binarylane.api.domains.post_v2_domains_refresh_nameserver_cache import sync_detailed

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import Mapping
from binarylane.console.runners.command import CommandRunner


class CommandRequest:
    pass


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "refresh-nameserver-cache"

    @property
    def description(self) -> str:
        return """Refresh Cached Nameserver Domain Records"""

    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/Domains/paths/~1v2~1domains~1refresh_nameserver_cache/post"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)
        return mapping

    @property
    def ok_response_type(self) -> type:
        return type(None)

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[None, Any]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.NO_CONTENT: Any
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            client=client,
        )
        return page_response.status_code, page_response.parsed
