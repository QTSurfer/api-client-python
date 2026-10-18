from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WalkForwardAccepted")


@_attrs_define
class WalkForwardAccepted:
    """Echo of the accepted walk-forward configuration, present only when the submit carried one. `inSamplePct` is the
    resolved value, so a request that omitted it can see what it got.

        Attributes:
            folds (int):
            in_sample_pct (int):
            total_runs (int): What this sweep actually costs, `folds × (grid size + 1)` — the in-sample runs for every fold
                plus each fold's one out-of-sample run. Deliberately distinct from the top-level `totalRuns`, which stays the
                size of the grid that was submitted.
    """

    folds: int
    in_sample_pct: int
    total_runs: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        folds = self.folds

        in_sample_pct = self.in_sample_pct

        total_runs = self.total_runs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "folds": folds,
                "inSamplePct": in_sample_pct,
                "totalRuns": total_runs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        folds = d.pop("folds")

        in_sample_pct = d.pop("inSamplePct")

        total_runs = d.pop("totalRuns")

        walk_forward_accepted = cls(
            folds=folds,
            in_sample_pct=in_sample_pct,
            total_runs=total_runs,
        )

        walk_forward_accepted.additional_properties = d
        return walk_forward_accepted

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
