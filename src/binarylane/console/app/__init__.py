""" app contains the the binarylane CLI entrypoint and local commands"""
from __future__ import annotations

import sys

from binarylane.console.app.app import App


def main() -> int:
    """CLI entrypoint"""
    App().run(sys.argv[1:])
    return 0
