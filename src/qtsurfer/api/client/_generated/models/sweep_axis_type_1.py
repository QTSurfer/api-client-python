from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="SweepAxisType1")


@_attrs_define
class SweepAxisType1:
    """
    Attributes:
        values (list[bool | float]):
    """

    values: list[bool | float]

    def to_dict(self) -> dict[str, Any]:
        values = []
        for values_item_data in self.values:
            values_item: bool | float
            values_item = values_item_data
            values.append(values_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "values": values,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        values = []
        _values = d.pop("values")
        for values_item_data in _values:

            def _parse_values_item(data: object) -> bool | float:
                return cast(bool | float, data)

            values_item = _parse_values_item(values_item_data)

            values.append(values_item)

        sweep_axis_type_1 = cls(
            values=values,
        )

        return sweep_axis_type_1
