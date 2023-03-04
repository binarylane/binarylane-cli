from __future__ import annotations

from enum import Enum
from typing import Optional
from binarylane.pycompat.typing import Protocol


class Option(str, Enum):
    API_URL = "api-url"
    API_TOKEN = "api-token"
    API_DEVELOPMENT = "api-development"
    CONFIG_SECTION = "context"


class Source(Protocol):
    def get(self, name: Option) -> Optional[str]:
        ...
