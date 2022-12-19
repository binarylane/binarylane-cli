from enum import Enum


class AlgorithmType(str, Enum):
    ROUND_ROBIN = "round_robin"
    LEAST_CONNECTIONS = "least_connections"

    def __str__(self) -> str:
        return str(self.value)
