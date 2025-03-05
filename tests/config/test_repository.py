from __future__ import annotations

from argparse import Namespace
from typing import TYPE_CHECKING, MutableMapping, Optional

import pytest

from binarylane.config import OptionName, Repository
from binarylane.config.sources import CommandlineSource, DefaultSource, EnvironmentSource, FileSource, RuntimeSource

if TYPE_CHECKING:
    from pathlib import Path


def test_init_default_source() -> None:
    repo = Repository()
    assert isinstance(repo.get_source(DefaultSource), DefaultSource)

    for source in (CommandlineSource, EnvironmentSource, FileSource, RuntimeSource):
        with pytest.raises(Exception):
            repo.get_source(source)


def test_init_no_default_source() -> None:
    repo = Repository(default_source=False)

    for source in (CommandlineSource, DefaultSource, EnvironmentSource, FileSource, RuntimeSource):
        with pytest.raises(Exception):
            repo.get_source(source)


def test_get_added_source_returns_source() -> None:
    source = RuntimeSource({})
    repo = Repository()

    repo.add_source(source)
    assert repo.get_source(RuntimeSource) is source


def test_get_source_returns_newest_of_type() -> None:
    source1 = RuntimeSource({})
    source2 = RuntimeSource({})

    repo = Repository()
    repo.add_source(source1)
    repo.add_source(source2)
    assert repo.get_source(RuntimeSource) is source2


def test_get_unadded_source_raises_key_error() -> None:
    repo = Repository()
    with pytest.raises(KeyError, match="RuntimeSource"):
        repo.get_source(RuntimeSource)


def test_add_option_adds_runtime_source() -> None:
    repo = Repository()

    repo.add_option(OptionName.API_TOKEN, "option_token")
    assert isinstance(repo.get_source(RuntimeSource), RuntimeSource)


def test_get_option() -> None:
    repo = Repository()
    assert repo.get_option(OptionName.API_TOKEN) is None

    repo.add_option(OptionName.API_TOKEN, "test")
    assert repo.get_option(OptionName.API_TOKEN) == "test"


def test_required_option() -> None:
    repo = Repository()
    with pytest.raises(KeyError):
        assert repo.required_option(OptionName.API_TOKEN)

    repo.add_option(OptionName.API_TOKEN, "required")
    assert repo.required_option(OptionName.API_TOKEN) == "required"


def create_repo(config_file: Optional[Path] = None, commandline: Optional[Namespace] = None) -> Repository:
    repo = Repository()
    if config_file:
        repo.add_source(FileSource(config_file))
    repo.add_source(EnvironmentSource())
    if commandline:
        repo.add_source(CommandlineSource(commandline))
    return repo


def test_get_option_prefers_newer_source() -> None:
    repo = Repository()
    repo.add_source(RuntimeSource({OptionName.API_URL: "first", OptionName.API_TOKEN: "first"}))
    repo.add_source(RuntimeSource({OptionName.API_TOKEN: "second", OptionName.CONFIG_SECTION: "second"}))

    # Second config did not provide a value for api_url, so it is still "first"
    assert repo.get_option(OptionName.API_URL) == "first"

    # Second config has priority for these values
    assert repo.get_option(OptionName.API_TOKEN) == "second"
    assert repo.get_option(OptionName.CONFIG_SECTION) == "second"


def test_environment_has_priority_over_file(tmp_path: Path, tmp_env: MutableMapping[str, str]) -> None:
    config_file = tmp_path / "config.ini"
    with open(config_file, "w") as file:
        file.write(
            """\
[bl]
api-token = file
"""
        )

    repo = create_repo(config_file)
    assert repo.get_option(OptionName.API_TOKEN) == "file"

    tmp_env["BL_API_TOKEN"] = "env"
    repo = create_repo(config_file)
    assert repo.get_option(OptionName.API_TOKEN) == "env"


def test_commandline_has_priority_over_environment(tmp_env: MutableMapping[str, str]) -> None:
    tmp_env["BL_API_TOKEN"] = "env"
    repo = create_repo()
    assert repo.get_option(OptionName.API_TOKEN) == "env"

    commandline = Namespace()
    commandline.api_token = "commandline"
    repo = create_repo(commandline=commandline)
    assert repo.get_option(OptionName.API_TOKEN) == "commandline"
