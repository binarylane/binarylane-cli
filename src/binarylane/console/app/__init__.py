from __future__ import annotations

import logging
import sys

from binarylane.console.app.app import App

logger = logging.getLogger(__name__)


def main() -> int:
    try:
        logging.basicConfig()
        App().run(sys.argv[1:])
        return 0

    # pylint: disable=broad-except
    except Exception as exc:
        logger.exception(exc)
        return -1
