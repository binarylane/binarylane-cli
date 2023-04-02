from __future__ import annotations

from platform import machine, python_implementation, python_version, system
from typing import TYPE_CHECKING

from binarylane.client import AuthenticatedClient

from binarylane.console.metadata import distribution_name, distribution_version

if TYPE_CHECKING:
    from binarylane.config import UserConfig


def create_client(config: UserConfig) -> AuthenticatedClient:
    return AuthenticatedClient(
        base_url=config.api_url,
        token=config.api_token,
        verify_ssl=not config.api_development,
        timeout=5.0,
        raise_on_unexpected_status=False,
        headers={"User-Agent": get_user_agent()},
    )


def get_user_agent() -> str:
    # example result: "binarylane-cli/0.13.0 (Linux/x86_64) CPython/3.10.6"
    user_agent = (
        f"{distribution_name()}/{distribution_version()}",
        f"({system()}/{machine()})",
        f"{python_implementation()}/{python_version()}",
    )

    return " ".join(user_agent)
