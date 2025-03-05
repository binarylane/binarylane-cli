from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from binarylane.console.app import App

if TYPE_CHECKING:
    from binarylane.console.runners import Context


class AppWithContext(App):
    def get_context(self) -> Context:
        return self._context


@pytest.fixture
def app() -> AppWithContext:
    return AppWithContext()
