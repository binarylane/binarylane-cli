from __future__ import annotations

def program_name():
    return "bl"

def program_description():
    return "bl is a command-line interface for the BinaryLane API"

def distribution_name():
    return "binarylane-cli"

def distribution_version() -> str:
    from binarylane.pycompat.importlib import metadata
    
    try:
        return metadata.distribution(distribution_name()).version
    except metadata.PackageNotFoundError:
        return "dev"