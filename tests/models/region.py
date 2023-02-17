from __future__ import annotations

from typing import Any, Dict, List

import attr


@attr.s(auto_attribs=True)
class Region:
    slug: str
    name: str
    sizes: List[str]
    available: bool
    features: List[str]
    name_servers: List[str]

    def to_dict(self) -> Dict[str, Any]:
        slug = self.slug
        name = self.name
        sizes = self.sizes

        available = self.available
        features = self.features

        name_servers = self.name_servers

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "slug": slug,
                "name": name,
                "sizes": sizes,
                "available": available,
                "features": features,
                "name_servers": name_servers,
            }
        )

        return field_dict
