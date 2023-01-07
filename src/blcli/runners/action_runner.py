import shutil
import sys
import time
from typing import Any, List, Optional

from ..cli import warn
from .command_runner import CommandRunner


class ActionRunner(CommandRunner):
    """ActionRunner handles API commands that return ActionResponse, showing progress until the Action completes"""

    _async: Optional[bool]

    def run(self, args: List[str]) -> None:
        self._parser.add_argument(
            "--async", action="store_true", dest="runner_async", help="Do not wait for requested action to complete"
        )
        super().run(args)

    def process(self, parsed: Any) -> None:
        self._async = parsed.runner_async
        super().process(parsed)

    def response(self, status_code: int, received: Any) -> None:
        # If async is requested, use standard handler
        if self._async:
            super().response(status_code, received)
            return

        # Delayed import for CLI performance
        # pylint: disable=import-outside-toplevel
        from ..client.api.action.action_get import sync_detailed
        from ..client.models.action_response import ActionResponse

        # Used to wipe existing output
        blanks = " " * (shutil.get_terminal_size().columns - 1)

        # Sit and wait for completion
        while isinstance(received, ActionResponse):
            step = received.action.progress.current_step or "Starting"
            status = f"{received.action.type}: {step} ({received.action.progress.percent_complete}%) ... "
            print(f"\r{blanks}\r{status}", end="", file=sys.stderr)

            if received.action.completed_at:
                print(f"{received.action.status}.", file=sys.stderr)
                break

            time.sleep(5)
            response = sync_detailed(received.action.id, client=self._client)
            status_code, received = response.status_code, response.parsed

        else:
            warn("Failed to get action")
            super().response(status_code, received)
        return
