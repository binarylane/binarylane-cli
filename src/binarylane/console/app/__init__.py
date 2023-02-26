from __future__ import annotations

import logging
import os
import sys
from typing import List

from binarylane.console.app.app import AppRunner
from binarylane.console.runners import Context

logger = logging.getLogger(__name__)


class App:
    context: Context

    def __init__(self) -> None:
        self.context = Context()
        self.runner = AppRunner(self.context)

    def run(self, args: List[str]) -> None:
        self.runner.run(args)


def main() -> int:
    try:
        # Support enabling debug logging via env var, since we may want to debug parsing of command line
        level = logging.WARNING if not os.getenv("BL_DEBUG") else logging.DEBUG
        logging.basicConfig(level=level)

        App().run(sys.argv[1:])
        return 0

    # pylint: disable=broad-except
    except Exception as exc:
        logger.exception(exc)
        return -1
