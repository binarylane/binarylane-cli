from enum import Enum


class ImageQueryType(str, Enum):
    DISTRIBUTION = "distribution"
    APPLICATION = "application"
    BACKUP = "backup"

    def __str__(self) -> str:
        return str(self.value)
