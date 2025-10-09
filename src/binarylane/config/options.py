from __future__ import annotations

from abc import ABC, abstractmethod
from configparser import ConfigParser
from enum import Enum
from typing import ClassVar, Optional


class OptionName(str, Enum):
    # Existing API options
    API_URL = "api-url"
    API_TOKEN = "api-token"
    API_DEVELOPMENT = "api-development"
    CONFIG_SECTION = "context"

    # Output preferences
    OUTPUT_FORMAT = "output-format"
    SHOW_HEADER = "show-header"

    # Per-command format preferences
    FORMAT_IMAGES = "format-images"
    FORMAT_SERVERS = "format-servers"
    FORMAT_DOMAINS = "format-domains"
    FORMAT_VPCS = "format-vpcs"
    FORMAT_LOAD_BALANCERS = "format-load-balancers"
    FORMAT_SSH_KEYS = "format-ssh-keys"
    FORMAT_ACTIONS = "format-actions"
    FORMAT_SIZES = "format-sizes"
    FORMAT_REGIONS = "format-regions"
    FORMAT_INVOICES = "format-invoices"
    FORMAT_SOFTWARE = "format-software"

    # Server creation defaults
    DEFAULT_REGION = "default-region"
    DEFAULT_SIZE = "default-size"
    DEFAULT_IMAGE = "default-image"
    DEFAULT_BACKUPS = "default-backups"
    DEFAULT_SSH_KEYS = "default-ssh-keys"
    DEFAULT_USER_DATA = "default-user-data"
    DEFAULT_PORT_BLOCKING = "default-port-blocking"
    DEFAULT_PASSWORD = "default-password"
    DEFAULT_VPC = "default-vpc"

    # Terminal settings
    TERMINAL_WIDTH = "terminal-width"

    def __str__(self) -> str:
        return self.value


class OptionAttributes(ABC):
    """Typed access to value of each configuration option"""

    UNCONFIGURED_TOKEN: ClassVar[str] = "unconfigured"

    @abstractmethod
    def get_option(self, name: OptionName) -> Optional[str]: ...

    @abstractmethod
    def required_option(self, name: OptionName) -> str: ...

    @abstractmethod
    def add_option(self, name: OptionName, value: str) -> None: ...

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

    # Output preference properties

    @property
    def output_format(self) -> Optional[str]:
        return self.get_option(OptionName.OUTPUT_FORMAT)

    @property
    def show_header(self) -> Optional[bool]:
        value = self.get_option(OptionName.SHOW_HEADER)
        return self.to_bool(value) if value else None

    # Per-command format preference properties

    @property
    def format_images(self) -> Optional[str]:
        return self.get_option(OptionName.FORMAT_IMAGES)

    @property
    def format_servers(self) -> Optional[str]:
        return self.get_option(OptionName.FORMAT_SERVERS)

    @property
    def format_domains(self) -> Optional[str]:
        return self.get_option(OptionName.FORMAT_DOMAINS)

    @property
    def format_vpcs(self) -> Optional[str]:
        return self.get_option(OptionName.FORMAT_VPCS)

    @property
    def format_load_balancers(self) -> Optional[str]:
        return self.get_option(OptionName.FORMAT_LOAD_BALANCERS)

    @property
    def format_ssh_keys(self) -> Optional[str]:
        return self.get_option(OptionName.FORMAT_SSH_KEYS)

    @property
    def format_actions(self) -> Optional[str]:
        return self.get_option(OptionName.FORMAT_ACTIONS)

    @property
    def format_sizes(self) -> Optional[str]:
        return self.get_option(OptionName.FORMAT_SIZES)

    @property
    def format_regions(self) -> Optional[str]:
        return self.get_option(OptionName.FORMAT_REGIONS)

    @property
    def format_invoices(self) -> Optional[str]:
        return self.get_option(OptionName.FORMAT_INVOICES)

    @property
    def format_software(self) -> Optional[str]:
        return self.get_option(OptionName.FORMAT_SOFTWARE)

    # Server creation default properties

    @property
    def default_region(self) -> Optional[str]:
        return self.get_option(OptionName.DEFAULT_REGION)

    @property
    def default_size(self) -> Optional[str]:
        return self.get_option(OptionName.DEFAULT_SIZE)

    @property
    def default_image(self) -> Optional[str]:
        return self.get_option(OptionName.DEFAULT_IMAGE)

    @property
    def default_backups(self) -> Optional[bool]:
        value = self.get_option(OptionName.DEFAULT_BACKUPS)
        return self.to_bool(value) if value else None

    @property
    def default_ssh_keys(self) -> Optional[str]:
        return self.get_option(OptionName.DEFAULT_SSH_KEYS)

    @property
    def default_user_data(self) -> Optional[str]:
        return self.get_option(OptionName.DEFAULT_USER_DATA)

    @property
    def default_port_blocking(self) -> Optional[bool]:
        value = self.get_option(OptionName.DEFAULT_PORT_BLOCKING)
        return self.to_bool(value) if value else None

    @property
    def default_password(self) -> Optional[str]:
        return self.get_option(OptionName.DEFAULT_PASSWORD)

    @property
    def default_vpc(self) -> Optional[str]:
        return self.get_option(OptionName.DEFAULT_VPC)

    # Terminal setting properties

    @property
    def terminal_width(self) -> Optional[int]:
        value = self.get_option(OptionName.TERMINAL_WIDTH)
        if value and value.lower() != "auto":
            try:
                return int(value)
            except ValueError:
                return None
        return None
