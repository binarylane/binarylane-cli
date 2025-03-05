from __future__ import annotations

from typing import Any, Dict

import attr

from binarylane.models.pages import Pages


@attr.s(auto_attribs=True)
class Links:
    pages: Pages

    def to_dict(self) -> Dict[str, Any]:
        pages = self.pages.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "pages": pages,
            }
        )

        return field_dict
