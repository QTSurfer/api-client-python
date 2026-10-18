from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sweep_marginal_point import SweepMarginalPoint


T = TypeVar("T", bound="SweepMarginal")


@_attrs_define
class SweepMarginal:
    """One axis, with every other axis collapsed away.

    Attributes:
        param (str | Unset):
        points (list[SweepMarginalPoint] | Unset):
    """

    param: str | Unset = UNSET
    points: list[SweepMarginalPoint] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        param = self.param

        points: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.points, Unset):
            points = []
            for points_item_data in self.points:
                points_item = points_item_data.to_dict()
                points.append(points_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if param is not UNSET:
            field_dict["param"] = param
        if points is not UNSET:
            field_dict["points"] = points

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sweep_marginal_point import SweepMarginalPoint

        d = dict(src_dict)
        param = d.pop("param", UNSET)

        _points = d.pop("points", UNSET)
        points: list[SweepMarginalPoint] | Unset = UNSET
        if _points is not UNSET:
            points = []
            for points_item_data in _points:
                points_item = SweepMarginalPoint.from_dict(points_item_data)

                points.append(points_item)

        sweep_marginal = cls(
            param=param,
            points=points,
        )

        sweep_marginal.additional_properties = d
        return sweep_marginal

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
