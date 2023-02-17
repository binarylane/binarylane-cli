from typing import Any, Dict

import attr


@attr.s(auto_attribs=True)
class Host:
    display_name: str

    def to_dict(self) -> Dict[str, Any]:
        display_name = self.display_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "display_name": display_name,
            }
        )
        return field_dict
