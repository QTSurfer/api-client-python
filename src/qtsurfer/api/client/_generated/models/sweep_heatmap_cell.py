from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SweepHeatmapCell")


@_attrs_define
class SweepHeatmapCell:
    """
    Attributes:
        value_a (Any | Unset):
        value_b (Any | Unset):
        count (int | Unset):
        best (float | Unset):
        mean (float | Unset):
    """

    value_a: Any | Unset = UNSET
    value_b: Any | Unset = UNSET
    count: int | Unset = UNSET
    best: float | Unset = UNSET
    mean: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value_a = self.value_a

        value_b = self.value_b

        count = self.count

        best = self.best

        mean = self.mean

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value_a is not UNSET:
            field_dict["valueA"] = value_a
        if value_b is not UNSET:
            field_dict["valueB"] = value_b
        if count is not UNSET:
            field_dict["count"] = count
        if best is not UNSET:
            field_dict["best"] = best
        if mean is not UNSET:
            field_dict["mean"] = mean

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value_a = d.pop("valueA", UNSET)

        value_b = d.pop("valueB", UNSET)

        count = d.pop("count", UNSET)

        best = d.pop("best", UNSET)

        mean = d.pop("mean", UNSET)

        sweep_heatmap_cell = cls(
            value_a=value_a,
            value_b=value_b,
            count=count,
            best=best,
            mean=mean,
        )

        sweep_heatmap_cell.additional_properties = d
        return sweep_heatmap_cell

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
