from __future__ import annotations

import logging
from abc import abstractmethod
from http import HTTPStatus
from typing import Any, List, Optional, Tuple

from binarylane.client import AuthenticatedClient, Client

from binarylane.console.config import Option
from binarylane.console.context import Context
from binarylane.console.parser import Mapping
from binarylane.console.parser.parser import Parser
from binarylane.console.printers import Printer, PrinterType, create_printer
from binarylane.console.runners import Runner
from binarylane.console.runners.httpx_wrapper import CurlCommand

logger = logging.getLogger(__name__)


class CommandRunner(Runner):
    """CommandRunner parses input, executes API operation and displays the result"""

    _parser: Parser
    _client: AuthenticatedClient

    _print_curl: Optional[bool]
    _output: Optional[str]
    _header: Optional[bool]

    def __init__(self, context: Context) -> None:
        super().__init__(context)
        prog = f"{self.context.prog} {self.name}"
        self._parser = Parser(prog=prog, description=self.description, epilog=self._epilog)
        self.configure(self._parser)

        self._parser.add_argument(
            "--help", dest="runner_print_help", action="help", help="Display command options and descriptions"
        )
        self._parser.add_argument(
            "--curl", dest="runner_print_curl", action="store_true", help="Display API request as a 'curl' command-line"
        )
        self._parser.add_argument(
            "--no-header",
            dest="runner_header",
            action="store_false",
            default=True,
            help="Display columns without field labels",
        )
        printers = tuple(item.name.lower() for item in PrinterType)
        self._parser.add_argument(
            "--output",
            dest="runner_output",
            default="table",
            metavar="OUTPUT",
            choices=printers,
            help='Desired output format [%(choices)s] (Default: "%(default)s")',
        )
        self._output = None
        self._header = None

        self._parser.configure()

    @abstractmethod
    def create_mapping(self) -> Mapping:
        """Add supported CLI arguments"""

    def configure(self, parser: Parser) -> None:
        mapping = self.create_mapping()
        parser.set_mapping(mapping)

    @abstractmethod
    def request(self, client: Client, request: object) -> Tuple[HTTPStatus, object]:
        """Perform API operation and return response"""

    @property
    @abstractmethod
    def ok_response_type(self) -> type:
        """The type returned by API for HTTP 200"""

    @property
    @abstractmethod
    def reference_url(self) -> str:
        """URL of reference documentation for this command"""

    @property
    def _printer(self) -> Printer:
        """Create printer of requested type"""
        if self._output is None or self._header is None:
            raise ValueError(f"output={self._output} header={self._header}")
        printer = create_printer(self._output)
        printer.header = self._header
        return printer

    @property
    def _epilog(self) -> str:
        return f"* API Documentation: {self.reference_url}\n"

    def response(self, status_code: int, received: Any) -> None:
        """Format and display response received from API operation"""
        if status_code == 401:
            self.error('Unable to authenticate with API - please run "bl configure" to get started.')
        elif received:
            self._printer.print(received)
        elif status_code != 204:
            self.error(f"HTTP {status_code}")

    def process(self, parsed: Any) -> None:
        """Process runner-local arguments"""

        self._print_curl = parsed.runner_print_curl
        if self._output is None:
            self._output = parsed.runner_output
        if self._header is None:
            self._header = parsed.runner_header

        for key in list(vars(parsed)):
            if key.startswith("runner_"):
                del parsed.__dict__[key]

    def run(self, args: List[str]) -> None:
        # Checks have already been performed during __init__
        if args == [Runner.CHECK]:
            return

        logger.debug("Command parser for %s. args: %s", self.name, args)
        parsed = self._parser.parse(args)
        logger.debug("Parsing succeeded, have %s", parsed)

        self.process(parsed)

        # NOTE: on handling when `ctx.get(Setting.ApiToken) is None` - i.e. has not been provided:
        #
        # 1. The code-generated endpoints currently all have AuthenticatedClient as a parameter, regardless of
        #    whether the given endpoint actually requires authentication, however there are endpoints returning
        #    non-customer specific information like `bl size list`, `bl region list` that do not require
        #    authentication to get a HTTP 200 response from. For this reason, we currently must create an
        #    AuthenticatedClient() object for every request.
        # 2. The code-generated AuthenticatedClient is generated with `token:  `str` rather than `Optional[str]`
        #    which makes sense, so we need to provide /a/ str.
        # 3. If token is "" then httpx will raise LocalProtocolError about the "Authorization: Bearer " header.
        # 4. If static type-checking is ignored and AuthenticatedClient is provided with `token=None`, then
        #    that value is coerced to str resulting in "Authorization: Bearer None" but that will look like a bug.
        # 5. Since "" is not accepted by httpx, for clarity we use a value of "unconfigured" for this situation.
        # 6. If the called endpoint does require an API token the response will be HTTP 401. Our response() method
        #    will then display a message requesting a token be provided via `bl configure`. If endpoint is
        #    publically accessable, the "Authorization: Bearer unconfigured" header is ignored and the response
        #    will be HTTP 200, which can then be processed as normal.
        #
        # TLDR: when user has not provided an API token, because of current limitations with generated
        # client library we cannot know whether a given endpoint requires authorization or is publically accessible,
        # so we use "Authorization: Bearer unconfigured" and handle whatever HTTP response the endpoint provides.
        #
        # If point 1 is resolved in the future, when user has not provided a token and code generation correctly
        # indicates that authorization is required we can skip the API call entirely and immediately display the
        # message requesting `bl configure`; while public endpoints would use the token-less Client() instead.

        self._client = AuthenticatedClient(
            self.context[Option.API_URL],
            self.context.get(Option.API_TOKEN, "unconfigured"),
            verify_ssl=not self.context.get(Option.API_DEVELOPMENT),
        )
        parsed.client = self._client

        # CurlCommand does not execute the request, so there is no response to display
        if self._print_curl:
            with CurlCommand() as curl:
                self.request(parsed.client, parsed.mapped_object)
                print(curl.shell)
                return

        status_code, received = self.request(parsed.client, parsed.mapped_object)
        self.response(status_code, received)
