from __future__ import annotations

from typing import Optional, Protocol

from binarylane.console.config.option import Option


class Source(Protocol):
    def get(self, name: Option) -> Optional[str]:
        ...
