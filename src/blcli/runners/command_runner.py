from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, Any, Dict, List, Optional

from ..cli import CommandParser, debug, error
from ..config import Config
from ..printers import Printer, PrinterType, create_printer
from .httpx_wrapper import CurlCommand
from .runner import Runner

if TYPE_CHECKING:
    from ..client import AuthenticatedClient


class CommandRunner(Runner):
    """CommandRunner parses input, executes API operation and displays the result"""

    _parser: CommandParser
    _parent: Runner
    _config: Config
    _client: "AuthenticatedClient"

    _print_curl: Optional[bool]
    _output: Optional[str]
    _header: Optional[bool]

    def __init__(self, parent: Runner) -> None:
        super().__init__(parent)
        self._config = Config.load()
        self._parser = CommandParser(prog=self.prog, add_help=False)
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

    @abstractmethod
    def configure(self, parser: CommandParser) -> None:
        """Add supported CLI arguments"""

    @abstractmethod
    def request(self, **kwargs: Dict[str, Any]) -> Any:
        """Perform API operation and return response"""

    @property
    def _printer(self) -> Printer:
        """Create printer of requested type"""
        if self._output is None or self._header is None:
            raise ValueError(f"output={self._output} header={self._header}")
        printer = create_printer(self._output)
        printer.header = self._header
        return printer

    def response(self, status_code: int, received: Any) -> None:
        """Format and display response received from API operation"""
        if status_code == 401:
            error('Unable to authenticate with API - please run "bl configure" to get started.')
        elif received:
            self._printer.print(received)
        elif status_code != 204:
            error(f"HTTP {status_code}")

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
            return None

        debug(f"Command parser for {self.name}. args: {args}")
        parsed = self._parser.parse_args(args)
        debug(f"Parsing succeeded, have {parsed}")

        self.process(parsed)

        # pylint: disable=import-outside-toplevel
        from ..client import AuthenticatedClient

        self._client = AuthenticatedClient(
            self._config.api_url,
            self._config.api_token,
        )
        parsed.client = self._client

        request_args = vars(parsed)

        # CurlCommand does not execute the request, so there is no response to display
        if self._print_curl:
            with CurlCommand() as curl:
                self.request(**request_args)
                return print(curl.shell)

        return self.response(*self.request(**vars(parsed)))
