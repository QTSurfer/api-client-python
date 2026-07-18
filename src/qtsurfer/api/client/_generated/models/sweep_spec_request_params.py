from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.sweep_axis_type_0 import SweepAxisType0
    from ..models.sweep_axis_type_1 import SweepAxisType1


T = TypeVar("T", bound="SweepSpecRequestParams")


@_attrs_define
class SweepSpecRequestParams:
    """ """

    additional_properties: dict[str, SweepAxisType0 | SweepAxisType1] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.sweep_axis_type_0 import SweepAxisType0

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            if isinstance(prop, SweepAxisType0):
                field_dict[prop_name] = prop.to_dict()
            else:
                field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sweep_axis_type_0 import SweepAxisType0
        from ..models.sweep_axis_type_1 import SweepAxisType1

        d = dict(src_dict)
        sweep_spec_request_params = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(data: object) -> SweepAxisType0 | SweepAxisType1:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_sweep_axis_type_0 = SweepAxisType0.from_dict(data)

                    return componentsschemas_sweep_axis_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_sweep_axis_type_1 = SweepAxisType1.from_dict(data)

                return componentsschemas_sweep_axis_type_1

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        sweep_spec_request_params.additional_properties = additional_properties
        return sweep_spec_request_params

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> SweepAxisType0 | SweepAxisType1:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: SweepAxisType0 | SweepAxisType1) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
