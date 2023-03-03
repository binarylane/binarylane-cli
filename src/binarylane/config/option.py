from __future__ import annotations

from enum import Enum


class Option(str, Enum):
    API_URL = "api-url"
    API_TOKEN = "api-token"
    API_DEVELOPMENT = "api-development"
    CONFIG_SECTION = "context"
