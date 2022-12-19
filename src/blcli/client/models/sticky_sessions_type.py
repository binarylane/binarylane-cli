from enum import Enum


class StickySessionsType(str, Enum):
    NONE = "none"
    COOKIES = "cookies"

    def __str__(self) -> str:
        return str(self.value)
