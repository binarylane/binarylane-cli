from __future__ import annotations

from binarylane.console.runners import Runner


class LazyRunner(Runner):
    """LazyRunner is a Runner that is imported ondemand by LazyLoader"""

    proxy: Runner

    def __init__(self, context: Runner) -> None:
        super().__init__(context._context)
        self.proxy = context

    @property
    def name(self) -> str:
        return self.proxy.name

    @property
    def description(self) -> str:
        return self.proxy.description
