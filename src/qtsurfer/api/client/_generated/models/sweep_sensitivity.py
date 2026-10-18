from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sweep_sensitivity_objective import SweepSensitivityObjective
from ..models.sweep_sensitivity_status import SweepSensitivityStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sweep_heatmap import SweepHeatmap
    from ..models.sweep_marginal import SweepMarginal


T = TypeVar("T", bound="SweepSensitivity")


@_attrs_define
class SweepSensitivity:
    """Sensitivity aggregates over a sweep's stored rows. Marginals are always complete; heatmaps may be capped, in which
    case `heatmapsTruncated` is true.

        Attributes:
            sweep_id (str | Unset):
            status (SweepSensitivityStatus | Unset):
            objective (SweepSensitivityObjective | Unset):
            rows_analysed (int | Unset): Rows available when this was computed. Grows while a sweep is still running.
            marginals (list[SweepMarginal] | Unset):
            heatmaps (list[SweepHeatmap] | Unset):
            heatmaps_truncated (bool | Unset): True when at least one two-parameter surface was left out to stay inside the
                response budget. Told explicitly because a silently short list would read as "these are all the interactions",
                which is the wrong thing to conclude from a sensitivity view.
    """

    sweep_id: str | Unset = UNSET
    status: SweepSensitivityStatus | Unset = UNSET
    objective: SweepSensitivityObjective | Unset = UNSET
    rows_analysed: int | Unset = UNSET
    marginals: list[SweepMarginal] | Unset = UNSET
    heatmaps: list[SweepHeatmap] | Unset = UNSET
    heatmaps_truncated: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sweep_id = self.sweep_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        objective: str | Unset = UNSET
        if not isinstance(self.objective, Unset):
            objective = self.objective.value

        rows_analysed = self.rows_analysed

        marginals: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.marginals, Unset):
            marginals = []
            for marginals_item_data in self.marginals:
                marginals_item = marginals_item_data.to_dict()
                marginals.append(marginals_item)

        heatmaps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.heatmaps, Unset):
            heatmaps = []
            for heatmaps_item_data in self.heatmaps:
                heatmaps_item = heatmaps_item_data.to_dict()
                heatmaps.append(heatmaps_item)

        heatmaps_truncated = self.heatmaps_truncated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sweep_id is not UNSET:
            field_dict["sweepId"] = sweep_id
        if status is not UNSET:
            field_dict["status"] = status
        if objective is not UNSET:
            field_dict["objective"] = objective
        if rows_analysed is not UNSET:
            field_dict["rowsAnalysed"] = rows_analysed
        if marginals is not UNSET:
            field_dict["marginals"] = marginals
        if heatmaps is not UNSET:
            field_dict["heatmaps"] = heatmaps
        if heatmaps_truncated is not UNSET:
            field_dict["heatmapsTruncated"] = heatmaps_truncated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sweep_heatmap import SweepHeatmap
        from ..models.sweep_marginal import SweepMarginal

        d = dict(src_dict)
        sweep_id = d.pop("sweepId", UNSET)

        _status = d.pop("status", UNSET)
        status: SweepSensitivityStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SweepSensitivityStatus(_status)

        _objective = d.pop("objective", UNSET)
        objective: SweepSensitivityObjective | Unset
        if isinstance(_objective, Unset):
            objective = UNSET
        else:
            objective = SweepSensitivityObjective(_objective)

        rows_analysed = d.pop("rowsAnalysed", UNSET)

        _marginals = d.pop("marginals", UNSET)
        marginals: list[SweepMarginal] | Unset = UNSET
        if _marginals is not UNSET:
            marginals = []
            for marginals_item_data in _marginals:
                marginals_item = SweepMarginal.from_dict(marginals_item_data)

                marginals.append(marginals_item)

        _heatmaps = d.pop("heatmaps", UNSET)
        heatmaps: list[SweepHeatmap] | Unset = UNSET
        if _heatmaps is not UNSET:
            heatmaps = []
            for heatmaps_item_data in _heatmaps:
                heatmaps_item = SweepHeatmap.from_dict(heatmaps_item_data)

                heatmaps.append(heatmaps_item)

        heatmaps_truncated = d.pop("heatmapsTruncated", UNSET)

        sweep_sensitivity = cls(
            sweep_id=sweep_id,
            status=status,
            objective=objective,
            rows_analysed=rows_analysed,
            marginals=marginals,
            heatmaps=heatmaps,
            heatmaps_truncated=heatmaps_truncated,
        )

        sweep_sensitivity.additional_properties = d
        return sweep_sensitivity

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
