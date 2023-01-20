from __future__ import annotations

import logging
import os
import sys

from binarylane.console.app.app import App

logger = logging.getLogger(__name__)


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
