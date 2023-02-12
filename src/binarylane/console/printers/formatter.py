from __future__ import annotations

import logging
import typing
from typing import Any, Dict, List, Optional, Sequence, Union

logger = logging.getLogger(__name__)

NULL_STR = ""
META = {"additional_properties", "meta", "links"}
DEFAULT_HEADING = "response"


def format_response(response: Any, show_header: bool, fields: Optional[List[str]] = None) -> List[List[str]]:
    """Convert structured response object into a 'table' (where the length of each inner list is the same)"""

    primary = _extract_primary(response)
    primary_type = type(primary)

    if isinstance(primary, list):
        for key, value in getattr(primary_type, "__annotations__", {DEFAULT_HEADING: "value"}).items():
            logger.debug(
                "key=%(key)s value=%(value)s dict?%(is_dict)s origin:%(origin)s",
                {
                    "key": key,
                    "value": value,
                    "is_dict": hasattr(value, "to_dict"),
                    "origin": getattr(value, "__origin__", None),
                },
            )

        header = fields or [
            key
            for key, value in getattr(primary_type, "__annotations__", {"response": "value"}).items()
            if key != "additional_properties"
            and not hasattr(value, "to_dict")
            and not getattr(value, "__origin__", None) in (Union, list)
        ]

        def object_to_list(row: Dict[str, Any], columns: List[str]) -> List[Any]:
            """Extract each field in `columns` from `row` into a list, in the same order as `columns`"""
            return [row.get(prop) for prop in columns]

        data = [header] if show_header else []
        data += [
            _flatten([item] if isinstance(item, str) else object_to_list(item.to_dict(), header)) for item in primary
        ]

    elif isinstance(primary, str):
        data = [[DEFAULT_HEADING]] if show_header else []
        data += [[primary]]

    else:
        data = [["name", "value"]] if show_header else []
        data += [_flatten(item, True) for item in primary.to_dict().items()]

    return data


def _get_primary_candidates(response_type: Any) -> Dict[str, type]:
    type_hints = typing.get_type_hints(response_type)
    return {name: type_hint for name, type_hint in type_hints.items() if name not in META}


def check_response_type(response_type: type) -> bool:
    """Returns bool indicating if we understand how to format the response_type"""
    return len(_get_primary_candidates(response_type)) < 2


def _extract_primary(response: Any) -> Any:
    """Extract the object (which may be a list or individual model instance) from response

    If the response is a 'wrapper' type containing one model type (e.g. a list or single entity), we want to
    extract that while ignore the descriptor properties like meta, links, additional_properties.
    """

    response_type = type(response)
    type_hints = _get_primary_candidates(response_type)

    if len(type_hints) == 1:
        return getattr(response, list(type_hints.keys())[0])

    if len(type_hints) > 1:
        logger.warning("%s has multiple properties, displaying the whole response", response_type)
    return response


def _flatten(values: Sequence[Any], single_object: bool = False) -> List[str]:
    """Transform each item in values into a format more suitable for displaying"""

    result: List[str] = []
    max_list = 5
    max_str = 80 if not single_object else 240
    trunc = "..."

    for item in values:
        item_type = type(item)
        if item_type is list:
            if len(item) > max_list:
                item = item[:max_list] + [trunc]
            if not single_object:
                item = ", ".join(map(str, item))
            else:
                item = (
                    "- "
                    + "\n- ".join(
                        [
                            (
                                "  ".join(f"{key}: {value}\n" for key, value in i.items())
                                if isinstance(i, dict)
                                else str(i)
                            )
                            for i in item
                        ]
                    )
                    if item
                    else ""
                )
        if item_type is dict:
            item = _flatten_dict(item, single_object)

        if item_type is bool:
            item = "Yes" if item else "No"

        item = str(item) if item is not None else NULL_STR
        if len(item) > max_str + len(trunc):
            item = item[:max_str] + trunc
        result.append(item)

    return result


def _flatten_dict(item: Dict[str, Any], single_object: bool) -> str:
    # FIXME: openapi spec should provide these directions

    # - use display_name for host
    # - use full_name for image (preferred over name)
    # - of the remainder generic columns we prefer name > slug > id
    for key in ("display_name", "full_name", "name", "slug", "id"):
        if key in item:
            return item[key]

    # Map 'networks' dictionary to a list of primary IPv4+v6
    if not single_object and "v4" in item and "v6" in item:
        return "\n".join([entry["ip_address"] for entry in item["v4"][:1] + item["v6"][:1]])

    # Generic handler
    return "<object>" if not single_object else "\n".join([f"{key}: {value}" for key, value in item.items()])
