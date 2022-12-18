""" Command line interface for the BinaryLane API """
import importlib
import sys
import time
from typing import Any, Callable

from . import app, cli


def debug_time(func: Callable[[], Any], msg: str = None) -> None:
    """
    Time how long func takes to run, and write to debug log.
    :param func: the function to time
    :param msg: message to show in debug log next to the elapsed time
    """
    start = time.time()
    func()
    end = time.time()
    cli.debug(f"DEBUG: {int(1000 * (end - start))}ms for '{msg or repr(func)}'")
