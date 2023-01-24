from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Any, Tuple, Union

from binarylane.api.accounts.get_v2_account import sync_detailed
from binarylane.models.account_response import AccountResponse

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import Mapping
from binarylane.console.runners.command import CommandRunner


class CommandRequest:
    pass


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "get"

    @property
    def description(self) -> str:
        return """Fetch Information About the Current Account"""

    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/Accounts/paths/~1v2~1account/get"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)
        return mapping

    @property
    def ok_response_type(self) -> type:
        return AccountResponse

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[None, AccountResponse, Any]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.OK: AccountResponse
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            client=client,
        )
        return page_response.status_code, page_response.parsed
