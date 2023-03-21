from __future__ import annotations

import logging
from abc import abstractmethod
from http import HTTPStatus
from typing import Any, List, Optional, Tuple

from binarylane.client import AuthenticatedClient, Client

from binarylane.console.parser import Mapping, Namespace, Parser
from binarylane.console.printers import Printer, PrinterType, create_printer
from binarylane.console.runners import Runner
from binarylane.console.runners.httpx_wrapper import CurlCommand
from binarylane.console.util import create_client

logger = logging.getLogger(__name__)


class CommandRunner(Runner):
    """CommandRunner parses input, executes API operation and displays the result"""

    _parser: Parser
    _client: AuthenticatedClient

    _print_curl: Optional[bool]
    _output: Optional[str] = None
    _header: Optional[bool] = None

    @abstractmethod
    def create_mapping(self) -> Mapping:
        """Add supported CLI arguments"""

    def configure(self, parser: Parser) -> None:
        mapping = self.create_mapping()
        parser.set_mapping(mapping)

        parser.add_argument(
            "--curl", dest="runner_print_curl", action="store_true", help="Display API request as a 'curl' command-line"
        )
        parser.add_argument(
            "--no-header",
            dest="runner_header",
            action="store_false",
            default=True,
            help="Display columns without field labels",
        )
        printers = tuple(item.name.lower() for item in PrinterType)
        parser.add_argument(
            "--output",
            dest="runner_output",
            default="table",
            metavar="OUTPUT",
            choices=printers,
            help='Desired output format [%(choices)s] (default: "%(default)s")',
        )

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

        # No response can be due to a `204 No Content` response, but also when
        # a response is not documented
        if received is None:
            if status_code != 204:
                self.error(f"HTTP {status_code}")
            return

        # FIXME: use openapi response spec to determine how to handle errors
        if status_code >= 400 and received:
            # BinaryLane API does not have correct type on all errors - some are typed as ProblemDetails but
            # actually return ValidationProblemDetails - so need to handle when errors are in additionalProperties
            errors = received["errors"] if "errors" in received else getattr(received, "errors", None)

            if errors:
                # errors is a map of list of error messages, convert to a list of error messages
                for key in errors:
                    errors[key] = ", ".join([msg.lower().rstrip(".") for msg in errors[key]])
                self._parser.error("; ".join(f"argument {key.upper()}: {errors[key]}" for key in errors))

            # Otherwise, try and find a string we can display
            for attr in ("detail", "title"):
                value = getattr(received, attr, None)
                if value:
                    self._parser.error(value)

        if received:
            self._printer.print(received)
        elif status_code != 204:
            self.error(f"HTTP {status_code}")

    def process(self, parsed: Namespace) -> None:
        self._print_curl = parsed.runner_print_curl
        if self._output is None:
            self._output = parsed.runner_output
        if self._header is None:
            self._header = parsed.runner_header

    def run(self, args: List[str]) -> None:
        # Checks have already been performed during __init__
        if args == [self.CHECK]:
            return

        logger.debug("Command parser for %s. args: %s", self._context.name, args)
        parsed = self.parse(args)
        logger.debug("Parsing succeeded, have %s", parsed)

        self.process(parsed)
        self._client = create_client(self._context)

        # CurlCommand does not execute the request, so there is no response to display
        if self._print_curl:
            with CurlCommand() as curl:
                self.request(self._client, parsed.mapped_object)
                print(curl.shell)
                return

        status_code, received = self.request(self._client, parsed.mapped_object)
        self.response(status_code, received)
