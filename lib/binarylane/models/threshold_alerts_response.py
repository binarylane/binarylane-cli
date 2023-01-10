from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar

import attr

from binarylane.models.threshold_alert import ThresholdAlert

T = TypeVar("T", bound="ThresholdAlertsResponse")


@attr.s(auto_attribs=True)
class ThresholdAlertsResponse:
    """
    Attributes:
        threshold_alerts (List[ThresholdAlert]):
    """

    threshold_alerts: List[ThresholdAlert]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        threshold_alerts = []
        for threshold_alerts_item_data in self.threshold_alerts:
            threshold_alerts_item = threshold_alerts_item_data.to_dict()

            threshold_alerts.append(threshold_alerts_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "threshold_alerts": threshold_alerts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        threshold_alerts = []
        _threshold_alerts = d.pop("threshold_alerts")
        for threshold_alerts_item_data in _threshold_alerts:
            threshold_alerts_item = ThresholdAlert.from_dict(threshold_alerts_item_data)

            threshold_alerts.append(threshold_alerts_item)

        threshold_alerts_response = cls(
            threshold_alerts=threshold_alerts,
        )

        threshold_alerts_response.additional_properties = d
        return threshold_alerts_response

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
