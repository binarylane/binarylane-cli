from __future__ import annotations

from typing import Any

from binarylane.console.runners.action import ActionRunner


class ActionLinkRunner(ActionRunner):
    """ActionLinkRunner handles command responses with an optional action ID attached"""

    @property
    def _default_output(self) -> str:
        return "table"

    def response(self, status_code: int, received: Any) -> None:
        from binarylane.models.actions_links import ActionsLinks

        links = getattr(received, "links", None)
        if not isinstance(links, ActionsLinks) or not links.actions:
            super().response(status_code, received)
            return

        # Show action progress on stdout
        if not self._async:
            action_id = links.actions[0].id
            self.wait_for_action(status_code, action_id)

        # Print the 'other' object (e.g. server) from the response
        self._printer.print(received)
