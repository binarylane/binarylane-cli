""" Contains methods for accessing image endpoints """
from __future__ import annotations

from typing import List, Type

from ...runners import ModuleRunner

__all__ = ["commands"]
commands: List[Type[ModuleRunner]] = []


def register_command(cls: ModuleRunner) -> ModuleRunner:
    commands.append(cls)
    return cls


@register_command
class ImageList(ModuleRunner):
    """Runner for image_list API operation"""

    @property
    def name(self) -> str:
        return "list"

    @property
    def description(self) -> str:
        return "List All Images"

    @property
    def module_path(self) -> str:
        return ".commands.image.image_list"


@register_command
class ImageGet(ModuleRunner):
    """Runner for image_get API operation"""

    @property
    def name(self) -> str:
        return "get"

    @property
    def description(self) -> str:
        return "Fetch an Existing Image"

    @property
    def module_path(self) -> str:
        return ".commands.image.image_get"


@register_command
class ImageUpdate(ModuleRunner):
    """Runner for image_update API operation"""

    @property
    def name(self) -> str:
        return "update"

    @property
    def description(self) -> str:
        return "Update an Existing Image"

    @property
    def module_path(self) -> str:
        return ".commands.image.image_update"


@register_command
class ImageDownload(ModuleRunner):
    """Runner for image_download API operation"""

    @property
    def name(self) -> str:
        return "download"

    @property
    def description(self) -> str:
        return "Download an Existing Image"

    @property
    def module_path(self) -> str:
        return ".commands.image.image_download"
