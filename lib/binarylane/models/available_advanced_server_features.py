from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar

import attr

from binarylane.models.advanced_feature import AdvancedFeature
from binarylane.models.cpu_model import CpuModel
from binarylane.models.vm_machine_type import VmMachineType

T = TypeVar("T", bound="AvailableAdvancedServerFeatures")


@attr.s(auto_attribs=True)
class AvailableAdvancedServerFeatures:
    """
    Attributes:
        processor_models (List[CpuModel]): A list of the processor models available for this server.
        machine_types (List[VmMachineType]): A list of the machine types available for this server.
        advanced_features (List[AdvancedFeature]): A list of the advanced features available for this server.
    """

    processor_models: List[CpuModel]
    machine_types: List[VmMachineType]
    advanced_features: List[AdvancedFeature]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        processor_models = []
        for processor_models_item_data in self.processor_models:
            processor_models_item = processor_models_item_data.to_dict()

            processor_models.append(processor_models_item)

        machine_types = []
        for machine_types_item_data in self.machine_types:
            machine_types_item = machine_types_item_data.value

            machine_types.append(machine_types_item)

        advanced_features = []
        for advanced_features_item_data in self.advanced_features:
            advanced_features_item = advanced_features_item_data.value

            advanced_features.append(advanced_features_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "processor_models": processor_models,
                "machine_types": machine_types,
                "advanced_features": advanced_features,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        processor_models = []
        _processor_models = d.pop("processor_models")
        for processor_models_item_data in _processor_models:
            processor_models_item = CpuModel.from_dict(processor_models_item_data)

            processor_models.append(processor_models_item)

        machine_types = []
        _machine_types = d.pop("machine_types")
        for machine_types_item_data in _machine_types:
            machine_types_item = VmMachineType(machine_types_item_data)

            machine_types.append(machine_types_item)

        advanced_features = []
        _advanced_features = d.pop("advanced_features")
        for advanced_features_item_data in _advanced_features:
            advanced_features_item = AdvancedFeature(advanced_features_item_data)

            advanced_features.append(advanced_features_item)

        available_advanced_server_features = cls(
            processor_models=processor_models,
            machine_types=machine_types,
            advanced_features=advanced_features,
        )

        available_advanced_server_features.additional_properties = d
        return available_advanced_server_features

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
