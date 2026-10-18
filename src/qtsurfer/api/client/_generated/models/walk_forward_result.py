from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.walk_forward_fold import WalkForwardFold


T = TypeVar("T", bound="WalkForwardResult")


@_attrs_define
class WalkForwardResult:
    """Present only on a sweep submitted with `walkForward`, and present from acceptance onward — its presence, not its
    contents, is what identifies a walk-forward sweep. `completedFolds` is 0 while the first fold is still running.

        Attributes:
            folds (int): Folds requested at submit.
            completed_folds (int): Folds that have finished and reported a winner.
            results (list[WalkForwardFold]): One entry per completed fold, oldest first.
            in_sample_pct (int | Unset): Resolved in-sample share each fold optimized on.
            param_drift (float | Unset): Mean normalized lattice distance between consecutive fold winners. Low is good:
                winners that stay in a tight band fold after fold are evidence the parameter means something, while winners that
                jump across the grid every time are the sweep re-fitting noise, and that backtest will not survive contact with
                live data. **Absent is not zero** — the field is omitted whenever the figure could not be computed (fewer than
                two folds finished, no stored grid to place winners on), because zero is itself a meaningful reading here and a
                placeholder would be indistinguishable from perfect stability.
    """

    folds: int
    completed_folds: int
    results: list[WalkForwardFold]
    in_sample_pct: int | Unset = UNSET
    param_drift: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        folds = self.folds

        completed_folds = self.completed_folds

        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        in_sample_pct = self.in_sample_pct

        param_drift = self.param_drift

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "folds": folds,
                "completedFolds": completed_folds,
                "results": results,
            }
        )
        if in_sample_pct is not UNSET:
            field_dict["inSamplePct"] = in_sample_pct
        if param_drift is not UNSET:
            field_dict["paramDrift"] = param_drift

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.walk_forward_fold import WalkForwardFold

        d = dict(src_dict)
        folds = d.pop("folds")

        completed_folds = d.pop("completedFolds")

        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = WalkForwardFold.from_dict(results_item_data)

            results.append(results_item)

        in_sample_pct = d.pop("inSamplePct", UNSET)

        param_drift = d.pop("paramDrift", UNSET)

        walk_forward_result = cls(
            folds=folds,
            completed_folds=completed_folds,
            results=results,
            in_sample_pct=in_sample_pct,
            param_drift=param_drift,
        )

        walk_forward_result.additional_properties = d
        return walk_forward_result

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
