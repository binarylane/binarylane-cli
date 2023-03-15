from __future__ import annotations


def program_name() -> str:
    return "bl"


def program_description() -> str:
    return "bl is a command-line interface for the BinaryLane API"


def distribution_name() -> str:
    return "binarylane-cli"


def distribution_version() -> str:
    from binarylane.pycompat.importlib import metadata

    try:
        return metadata.distribution(distribution_name()).version
    except metadata.PackageNotFoundError:
        return "dev"
