from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SweepMarginalPoint")


@_attrs_define
class SweepMarginalPoint:
    """How the objective behaved at one value of one axis. `best` and `mean` disagreeing is informative rather than noise:
    a high `best` with a poor `mean` marks a value that only works alongside particular settings of the other axes.

        Attributes:
            value (Any | Unset): The axis value, as it appears in a run's parameters.
            count (int | Unset): Non-aborted runs that used this value.
            best (float | Unset):
            mean (float | Unset):
            worst (float | Unset):
    """

    value: Any | Unset = UNSET
    count: int | Unset = UNSET
    best: float | Unset = UNSET
    mean: float | Unset = UNSET
    worst: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        count = self.count

        best = self.best

        mean = self.mean

        worst = self.worst

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if count is not UNSET:
            field_dict["count"] = count
        if best is not UNSET:
            field_dict["best"] = best
        if mean is not UNSET:
            field_dict["mean"] = mean
        if worst is not UNSET:
            field_dict["worst"] = worst

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value", UNSET)

        count = d.pop("count", UNSET)

        best = d.pop("best", UNSET)

        mean = d.pop("mean", UNSET)

        worst = d.pop("worst", UNSET)

        sweep_marginal_point = cls(
            value=value,
            count=count,
            best=best,
            mean=mean,
            worst=worst,
        )

        sweep_marginal_point.additional_properties = d
        return sweep_marginal_point

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
