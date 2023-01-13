from __future__ import annotations

from http import HTTPStatus
from typing import Any, Tuple, Union

from binarylane.api.domain.domain_refresh_nameserver_cache import sync_detailed
from binarylane.client import Client

from binarylane.console.parsers import CommandParser
from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "refresh-nameserver-cache"

    @property
    def description(self) -> str:
        return """Refresh Cached Nameserver Domain Records"""

    def configure(self, parser: CommandParser) -> None:
        """Add arguments for domain_refresh-nameserver-cache"""

    @property
    def ok_response_type(self) -> type:
        return type(None)

    def request(
        self,
        client: Client,
    ) -> Tuple[HTTPStatus, Union[None, Any]]:

        # HTTPStatus.NO_CONTENT: Any
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            client=client,
        )
        return page_response.status_code, page_response.parsed
