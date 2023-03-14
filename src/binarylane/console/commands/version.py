from __future__ import annotations

from typing import List

from binarylane.console.runners import Runner
from binarylane.console.metadata import distribution_version


class Command(Runner):
    def run(self, args: List[str]) -> None:
        print(self._context.prog, distribution_version())
