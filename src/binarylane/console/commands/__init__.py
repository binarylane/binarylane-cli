from __future__ import annotations

from typing import List

from binarylane.console.commands import api
from binarylane.console.runners import Descriptor

__all__ = ["descriptors"]

# Filter out the auto-generated server create, we'll replace it with our wrapper
descriptors: List[Descriptor] = [d for d in api.descriptors if d.name != "server create"] + [
    Descriptor(".commands.configure", "configure", "Configure access to BinaryLane API"),
    Descriptor(".commands.preferences_get", "preferences get", "Display a preference value"),
    Descriptor(".commands.preferences_set", "preferences set", "Set or unset a preference value"),
    Descriptor(".commands.preferences_show", "preferences show", "Display preferences for a command or resource"),
    Descriptor(".commands.server_create", "server create", "Create a new server"),
    Descriptor(".commands.version", "version", "Show the current version"),
]
