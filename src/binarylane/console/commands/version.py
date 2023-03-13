from __future__ import annotations

from typing import List

from binarylane.console.runners import Runner
from binarylane.console.util import get_version


class Command(Runner):
    def run(self, args: List[str]) -> None:
        print(self._context.prog, get_version())
