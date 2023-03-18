from __future__ import annotations

from typing import Any, Dict

import attr


@attr.s(auto_attribs=True)
class Meta:
    total: int

    def to_dict(self) -> Dict[str, Any]:
        total = self.total

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "total": total,
            }
        )

        return field_dict
