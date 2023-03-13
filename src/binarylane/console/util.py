from __future__ import annotations

from binarylane.pycompat.importlib import metadata

from binarylane.client import AuthenticatedClient
from binarylane.config import Config


def get_version() -> str:
    try:
        return metadata.distribution("binarylane-cli").version
    except metadata.PackageNotFoundError:
        return "dev"


def create_client(config: Config) -> AuthenticatedClient:
    return AuthenticatedClient(
        base_url=config.api_url,
        token=config.api_token,
        verify_ssl=not config.api_development,
        timeout=5.0,
        raise_on_unexpected_status=False,
        headers={"User-Agent": f"binarylane-cli/{get_version()}"},
    )
