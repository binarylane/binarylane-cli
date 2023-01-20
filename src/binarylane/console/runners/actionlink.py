from __future__ import annotations

from typing import TYPE_CHECKING, Any

from binarylane.console.runners.action import ActionRunner

if TYPE_CHECKING:
    from binarylane.models.actions_links import ActionsLinks


class ActionLinkRunner(ActionRunner):
    """ActionLinkRunner handles command responses with an optional action ID attached"""

    def response(self, status_code: int, received: Any) -> None:

        from binarylane.models.actions_links import ActionsLinks

        links = getattr(received, "links", None)
        if not isinstance(links, ActionsLinks) or not links.actions:
            super().response(status_code, received)
            return

        action_id = links.actions[0].id
        super().response(status_code, action_id)

        # Print the 'other' object (e.g. server) from the response
        self._printer.print(received)
