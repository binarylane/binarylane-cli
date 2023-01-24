from __future__ import annotations

import logging
import shutil
import sys
import time
from typing import TYPE_CHECKING, Any, List, Optional

from binarylane.console.runners.command import CommandRunner

if TYPE_CHECKING:
    from binarylane.api.actions.get_v2_actions_action_id import sync_detailed
    from binarylane.models.action_response import ActionResponse

logger = logging.getLogger(__name__)


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
        if self._quiet:
            return

        if not sys.stderr.isatty():
            print(progress.rstrip("\n"), file=sys.stderr, flush=True)
            return

        # Used to wipe existing output
        blanks = " " * (shutil.get_terminal_size().columns - 1)
        print(f"\r{blanks}\r{progress}", end="", file=sys.stderr)

    def response(self, status_code: int, received: Any) -> None:
        # If async is requested, use standard handler
        if self._async:
            super().response(status_code, received)
            return

        from binarylane.api.actions.get_v2_actions_action_id import sync_detailed
        from binarylane.models.action_response import ActionResponse

        # FIXME: Extract _get_action(id: int) -> Tuple[int, Any] method so that derived class can call that instead
        # Derived class may provide an Action ID directly:
        if isinstance(received, int):
            response = sync_detailed(received, client=self._client)
            status_code, received = response.status_code, response.parsed

        # Sit and wait for completion
        while isinstance(received, ActionResponse):
            step = received.action.progress.current_step or "Starting"
            status = f"{received.action.type}: {step} ({received.action.progress.percent_complete}%) ... "
            self._progress(status)

            if received.action.completed_at:
                self._progress(f"{received.action.status}.\n")
                break

            time.sleep(5)
            response = sync_detailed(received.action.id, client=self._client)
            status_code, received = response.status_code, response.parsed

        else:
            logger.warning("Failed to get action")
            super().response(status_code, received)
        return
