from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sweep_heatmap_cell import SweepHeatmapCell


T = TypeVar("T", bound="SweepHeatmap")


@_attrs_define
class SweepHeatmap:
    """The surface for one pair of axes, with all others collapsed away.

    Attributes:
        param_a (str | Unset):
        param_b (str | Unset):
        cells (list[SweepHeatmapCell] | Unset):
    """

    param_a: str | Unset = UNSET
    param_b: str | Unset = UNSET
    cells: list[SweepHeatmapCell] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        param_a = self.param_a

        param_b = self.param_b

        cells: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.cells, Unset):
            cells = []
            for cells_item_data in self.cells:
                cells_item = cells_item_data.to_dict()
                cells.append(cells_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if param_a is not UNSET:
            field_dict["paramA"] = param_a
        if param_b is not UNSET:
            field_dict["paramB"] = param_b
        if cells is not UNSET:
            field_dict["cells"] = cells

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sweep_heatmap_cell import SweepHeatmapCell

        d = dict(src_dict)
        param_a = d.pop("paramA", UNSET)

        param_b = d.pop("paramB", UNSET)

        _cells = d.pop("cells", UNSET)
        cells: list[SweepHeatmapCell] | Unset = UNSET
        if _cells is not UNSET:
            cells = []
            for cells_item_data in _cells:
                cells_item = SweepHeatmapCell.from_dict(cells_item_data)

                cells.append(cells_item)

        sweep_heatmap = cls(
            param_a=param_a,
            param_b=param_b,
            cells=cells,
        )

        sweep_heatmap.additional_properties = d
        return sweep_heatmap

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
