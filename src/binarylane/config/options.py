from __future__ import annotations

from abc import ABC, abstractmethod
from configparser import ConfigParser
from enum import Enum
from typing import ClassVar, Optional


class OptionName(str, Enum):
    API_URL = "api-url"
    API_TOKEN = "api-token"
    API_DEVELOPMENT = "api-development"
    CONFIG_SECTION = "context"

    def __str__(self) -> str:
        return self.value


class OptionAttributes(ABC):
    """Typed access to value of each configuration option"""

    UNCONFIGURED_TOKEN: ClassVar[str] = "unconfigured"

    @abstractmethod
    def get_option(self, name: OptionName) -> Optional[str]:
        ...

    @abstractmethod
    def required_option(self, name: OptionName) -> str:
        ...

    @abstractmethod
    def add_option(self, name: OptionName, value: str) -> None:
        ...

    @staticmethod
    def to_bool(name: str) -> bool:
        value = ConfigParser.BOOLEAN_STATES.get(name.lower())
        if value is not None:
            return value
        raise ValueError(f"Not a boolean: {name}")

    @property
    def api_url(self) -> str:
        return self.required_option(OptionName.API_URL)

    @property
    def api_token(self) -> str:
        value = self.get_option(OptionName.API_TOKEN)

        # NOTE: on handling when `get(Option.API_TOKEN) is None` - i.e. has not been configured:
        #
        # 1. The code-generated endpoints currently all have AuthenticatedClient as a parameter, regardless of
        #    whether the given endpoint actually requires authentication, however there are endpoints returning
        #    non-customer specific information like `bl size list`, `bl region list` that do not require
        #    authentication to get a HTTP 200 response from. For this reason, we currently must create an
        #    AuthenticatedClient() object for every request.
        # 2. The code-generated AuthenticatedClient is generated with `token: str` rather than `Optional[str]`
        #    which makes sense, so we need to provide /something/.
        # 3. If token is "" then httpx will raise LocalProtocolError about the "Authorization: Bearer " header.
        # 4. If static type-checking is ignored and AuthenticatedClient is provided with `token=None`, then
        #    that value is coerced to str resulting in "Authorization: Bearer None" but that will look like a bug.
        # 5. Since "" is not accepted by httpx, for clarity we use a value of "unconfigured" for this situation.
        # 6. If the called endpoint does require an API token the response will be HTTP 401. Our response() method
        #    will then display a message requesting a token be provided via `bl configure`. If endpoint is
        #    publicly accessable, the "Authorization: Bearer unconfigured" header is ignored and the response
        #    will be HTTP 200, which can then be processed as normal.
        #
        # TLDR: when user has not provided an API token, because of current limitations with generated
        # client library we cannot know whether a given endpoint requires authorization or is publically accessible,
        # so we use "Authorization: Bearer unconfigured" and handle whatever HTTP response the endpoint provides.
        #
        # If point 1 is resolved in the future, when user has not provided a token and code generation correctly
        # indicates that authorization is required we can skip the API call entirely and immediately display the
        # message requesting `bl configure`; while public endpoints would use the token-less Client() instead.

        if value is None:
            return self.UNCONFIGURED_TOKEN
        return value

    @api_token.setter
    def api_token(self, value: str) -> None:
        self.add_option(OptionName.API_TOKEN, value)

    @property
    def api_development(self) -> bool:
        value = self.get_option(OptionName.API_DEVELOPMENT)
        if value is None:
            return False
        return self.to_bool(value)

    @property
    def config_section(self) -> str:
        return self.required_option(OptionName.CONFIG_SECTION)
