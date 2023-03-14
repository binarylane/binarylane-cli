from __future__ import annotations
from platform import system, machine, python_implementation, python_version
from binarylane.console.metadata import distribution_name, distribution_version


from binarylane.client import AuthenticatedClient
from binarylane.config import Config


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
    # example result: "binarylane-cli/0.13.0 (Linux/x86_64) CPython/3.10.6"
    user_agent = (
        f"{distribution_name()}/{distribution_version()}",
        f"({system()}/{machine()})",
        f"{python_implementation()}/{python_version()}",
    )

    return " ".join(user_agent)
