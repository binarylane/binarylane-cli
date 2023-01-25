from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from binarylane.models.advanced_feature import AdvancedFeature
from binarylane.models.video_device import VideoDevice
from binarylane.models.vm_machine_type import VmMachineType
from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="AdvancedServerFeatures")


@attr.s(auto_attribs=True)
class AdvancedServerFeatures:
    """
    Attributes:
        video_device (VideoDevice): Video Device

            | Value | Description |
            | ----- | ----------- |
            | cirrus-logic | Cirrus Logic GD5446 |
            | standard | Standard VGA with VESA 2.0 extensions |
            | virtio | Virtio VGA (800x600) |
            | virtio-wide | Virtio VGA (1600x900) |

        enabled_advanced_features (List[AdvancedFeature]): A list of the currently enabled advanced features for this
            server.
        processor_model (Union[Unset, None, str]): The ID of the processor model (and therefore CPU flags) available for
            this server.
            A null value indicates automatic selection of the best processor model supported by the host node.
            This does not change the physical CPU, only the CPU flags available to the operating system.
        machine_type (Union[Unset, None, VmMachineType]): The machine_type (corresponding to a KVM version) used for
            this server.
            A null value indicates automatic selection of the best KVM machine type supported by the host node.
    """

    video_device: VideoDevice
    enabled_advanced_features: List[AdvancedFeature]
    processor_model: Union[Unset, None, str] = UNSET
    machine_type: Union[Unset, None, VmMachineType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        video_device = self.video_device.value

        enabled_advanced_features = []
        for enabled_advanced_features_item_data in self.enabled_advanced_features:
            enabled_advanced_features_item = enabled_advanced_features_item_data.value

            enabled_advanced_features.append(enabled_advanced_features_item)

        processor_model = self.processor_model
        machine_type: Union[Unset, None, str] = UNSET
        if not isinstance(self.machine_type, Unset):
            machine_type = self.machine_type.value if self.machine_type else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "video_device": video_device,
                "enabled_advanced_features": enabled_advanced_features,
            }
        )
        if processor_model is not UNSET:
            field_dict["processor_model"] = processor_model
        if machine_type is not UNSET:
            field_dict["machine_type"] = machine_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        video_device = VideoDevice(d.pop("video_device"))

        enabled_advanced_features = []
        _enabled_advanced_features = d.pop("enabled_advanced_features")
        for enabled_advanced_features_item_data in _enabled_advanced_features:
            enabled_advanced_features_item = AdvancedFeature(enabled_advanced_features_item_data)

            enabled_advanced_features.append(enabled_advanced_features_item)

        processor_model = d.pop("processor_model", UNSET)

        _machine_type = d.pop("machine_type", UNSET)
        machine_type: Union[Unset, None, VmMachineType]
        if _machine_type is None:
            machine_type = None
        elif isinstance(_machine_type, Unset):
            machine_type = UNSET
        else:
            machine_type = VmMachineType(_machine_type)

        advanced_server_features = cls(
            video_device=video_device,
            enabled_advanced_features=enabled_advanced_features,
            processor_model=processor_model,
            machine_type=machine_type,
        )

        advanced_server_features.additional_properties = d
        return advanced_server_features

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
