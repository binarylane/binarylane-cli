from __future__ import annotations

from enum import Enum


class ResourceType(str, Enum):
    SERVER = "server"
    LOAD_BALANCER = "load-balancer"
    SSH_KEY = "ssh-key"
    VPC = "vpc"
    IMAGE = "image"
    REGISTERED_DOMAIN_NAME = "registered-domain-name"

    def __str__(self) -> str:
        return str(self.value)
