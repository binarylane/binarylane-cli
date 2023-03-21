from __future__ import annotations

import logging
from abc import abstractmethod
from http import HTTPStatus
from typing import Any, List, Optional, Tuple

from binarylane.client import AuthenticatedClient, Client
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails

from binarylane.console.parser import Mapping, Namespace, Parser
from binarylane.console.printers import Printer, PrinterType, create_printer
from binarylane.console.runners import ExitCode, Runner
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
            self.error(ExitCode.TOKEN, 'Unable to authenticate with API - please run "bl configure" to get started.')

        # No response can be due to a `204 No Content` response, but also when
        # a response is not documented
        if received is None:
            if status_code != 204:
                self.error(ExitCode.API, f"HTTP {status_code}")
            return

        # For successful responses, hand received object to printer
        if status_code < 300:
            self._printer.print(received)

        #
        # Otherwise, we have received an error response: extract relevant details for display
        #

        # BinaryLane API spec does not have currently have correct type on all errors - some are documented as
        # ProblemDetails but actually provide ValidationProblemDetails:
        if isinstance(received, ProblemDetails) and "errors" in received:
            received = ValidationProblemDetails.from_dict(received.to_dict())

        # If we have validation errors, combine them and display as parser error:
        if isinstance(received, ValidationProblemDetails) and received.errors:

            def list2str(value: List[str]) -> str:
                return ", ".join([msg.lower().rstrip(".") for msg in value])

            errors = {key: list2str(value) for key, value in received.errors.additional_properties.items()}
            self._parser.error("; ".join(f"argument {key.upper()}: {errors[key]}" for key in errors))

        # try and find a string we can display
        for attr in ("detail", "title"):
            value = getattr(received, attr, None)
            if value:
                self._parser.error(value)

        # Couldn't find anything, just provide the status code
        self.error(ExitCode.API, f"HTTP {status_code}")

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
