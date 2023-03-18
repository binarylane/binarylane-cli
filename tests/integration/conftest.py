from __future__ import annotations

import pytest

from binarylane.console.app import App
from binarylane.console.runners import Context


class AppWithContext(App):
    def get_context(self) -> Context:
        return self._context


@pytest.fixture
def app() -> AppWithContext:
    return AppWithContext()
