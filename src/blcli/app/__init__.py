""" app contains the the binarylane CLI entrypoint and local commands"""
import sys

from .app import App


def main() -> None:
    """CLI entrypoint"""
    App().run(sys.argv[1:])
