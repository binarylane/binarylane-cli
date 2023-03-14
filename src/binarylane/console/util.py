from __future__ import annotations
from platform import system, machine, python_implementation, python_version

from binarylane.pycompat.importlib import metadata

from binarylane.client import AuthenticatedClient
from binarylane.config import Config

DISTRIBUTION_NAME = "binarylane-cli"


def get_version() -> str:
    try:
        return metadata.distribution(DISTRIBUTION_NAME).version
    except metadata.PackageNotFoundError:
        return "dev"


def create_client(config: Config) -> AuthenticatedClient:
    return AuthenticatedClient(
        base_url=config.api_url,
        token=config.api_token,
        verify_ssl=not config.api_development,
        timeout=5.0,
        raise_on_unexpected_status=False,
        headers={"User-Agent": get_user_agent()},
    )


def get_user_agent():
    return f"{DISTRIBUTION_NAME}/{get_version()} ({system()}/{machine()}) {python_implementation()}/{python_version()}"
