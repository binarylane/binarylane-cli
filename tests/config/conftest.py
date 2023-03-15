from __future__ import annotations

import os
from typing import Iterator, MutableMapping

import pytest


@pytest.fixture
def tmp_env() -> Iterator[MutableMapping[str, str]]:
    environ = dict(os.environ)
    yield os.environ
    os.environ.clear()
    os.environ.update(environ)
