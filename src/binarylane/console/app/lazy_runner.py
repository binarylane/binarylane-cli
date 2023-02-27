from __future__ import annotations

from binarylane.console.runners import Runner


class LazyRunner(Runner):
    """LazyRunner is a Runner that is imported ondemand by LazyLoader"""

    # The loader provides our name and description
    loader: Runner

    def __init__(self, loader: Runner) -> None:
        super().__init__(loader.context)
        self.loader = loader

    @property
    def name(self) -> str:
        return self.loader.name

    @property
    def description(self) -> str:
        return self.loader.description
