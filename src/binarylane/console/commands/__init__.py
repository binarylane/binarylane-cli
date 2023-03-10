from __future__ import annotations

from typing import List, Type

from binarylane.console.commands import api
from binarylane.console.runners import Runner

__all__ = ["commands"]
commands: List[Type[Runner]] = list(api.commands)
