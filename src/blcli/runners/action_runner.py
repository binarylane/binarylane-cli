import shutil
import sys
import time
from typing import TYPE_CHECKING, Any, List, Optional

from ..cli import warn
from .command_runner import CommandRunner

if TYPE_CHECKING:
    from ..client.api.action.action_get import sync_detailed
    from ..client.models.action_response import ActionResponse


class ActionRunner(CommandRunner):
    """ActionRunner handles API commands that return ActionResponse, showing progress until the Action completes"""

    _async: Optional[bool]
    _quiet: Optional[bool]

    def run(self, args: List[str]) -> None:
        self._parser.add_argument(
            "--async", action="store_true", dest="runner_async", help="Do not wait for requested action to complete"
        )
        self._parser.add_argument(
            "--quiet",
            action="store_true",
            dest="runner_quiet",
            help="Do not show progress while waiting for requested action to complete",
        )
        super().run(args)

    def process(self, parsed: Any) -> None:
        self._async = parsed.runner_async
        self._quiet = parsed.runner_quiet
        super().process(parsed)

    def _progress(self, progress: str) -> None:
        if not self._quiet:
            print(progress, end="", file=sys.stderr)

    def response(self, status_code: int, received: Any) -> None:
        # If async is requested, use standard handler
        if self._async:
            super().response(status_code, received)
            return

        from ..client.api.action.action_get import sync_detailed
        from ..client.models.action_response import ActionResponse

        # FIXME: Extract _get_action(id: int) -> Tuple[int, Any] method so that derived class can call that instead
        # Derived class may provide an Action ID directly:
        if isinstance(received, int):
            response = sync_detailed(received, client=self._client)
            status_code, received = response.status_code, response.parsed

        # Used to wipe existing output
        blanks = " " * (shutil.get_terminal_size().columns - 1)

        # Sit and wait for completion
        while isinstance(received, ActionResponse):
            step = received.action.progress.current_step or "Starting"
            status = f"{received.action.type}: {step} ({received.action.progress.percent_complete}%) ... "
            self._progress(f"\r{blanks}\r{status}")

            if received.action.completed_at:
                self._progress(f"{received.action.status}.\n")
                break

            time.sleep(5)
            response = sync_detailed(received.action.id, client=self._client)
            status_code, received = response.status_code, response.parsed

        else:
            warn("Failed to get action")
            super().response(status_code, received)
        return
