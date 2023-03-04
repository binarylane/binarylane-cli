from __future__ import annotations

from pathlib import Path
from tempfile import NamedTemporaryFile, TemporaryDirectory

from binarylane.config import Option
from binarylane.config.sources import FileSource


def test_get() -> None:
    with NamedTemporaryFile() as file:
        file.write(
            """\
[bl]
api-token = test_token
""".encode()
        )
        file.flush()

        source = FileSource(Path(file.name))
        source.section_name = "bl"

        assert source.get(Option.API_TOKEN) == "test_token"


def test_absent() -> None:
    with TemporaryDirectory() as directory:
        config_file = Path(directory) / "config.ini"  # Does not exist
        source = FileSource(config_file)
        source.section_name = "bl"

        assert source.get(Option.API_TOKEN) is None
