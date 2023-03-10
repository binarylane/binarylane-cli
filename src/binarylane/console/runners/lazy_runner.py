from __future__ import annotations

from binarylane.console.runners import Runner


class LazyRunner(Runner):
    """LazyRunner is a Runner that is imported ondemand by LazyLoader"""

    proxy: Runner

    def __init__(self, parent: Runner) -> None:
        super().__init__(parent)
        self.proxy = parent

    @property
    def name(self) -> str:
        return self.proxy.name

    @property
    def description(self) -> str:
        return self.proxy.description
