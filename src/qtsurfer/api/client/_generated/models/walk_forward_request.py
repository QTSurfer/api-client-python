from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WalkForwardRequest")


@_attrs_define
class WalkForwardRequest:
    """Opt in to walk-forward validation. Present, the sweep runs as F sequential folds and the result gains a
    `walkForward` section; absent, nothing about the sweep changes. Two requests that differ only in this block are two
    different sweeps and do not deduplicate against each other.

        Attributes:
            folds (int): How many sequential optimize-then-score windows to run. Two is the minimum for a reason, and it is
                structural rather than a tuning choice: parameter drift is measured between consecutive fold winners, and a
                single fold — one train/test split with no sequence — has no consecutive pair to compare, so it would report the
                strongest possible stability having measured nothing.
                The upper bound is a server setting (12 by default) and is deliberately not pinned here, since a spec that
                hardcodes a tunable limit lies the day it is raised. Exceeding it, or exceeding the sweep budget once multiplied
                by the grid size, is a 400.
            in_sample_pct (int | Unset): Share of the session each fold spends optimizing; the remainder is where its winner
                is scored. Lower values leave more data to be scored on and, on short sessions, are also what lets the requested
                fold count tile the data at all. Default: 66.
    """

    folds: int
    in_sample_pct: int | Unset = 66
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        folds = self.folds

        in_sample_pct = self.in_sample_pct

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "folds": folds,
            }
        )
        if in_sample_pct is not UNSET:
            field_dict["inSamplePct"] = in_sample_pct

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        folds = d.pop("folds")

        in_sample_pct = d.pop("inSamplePct", UNSET)

        walk_forward_request = cls(
            folds=folds,
            in_sample_pct=in_sample_pct,
        )

        walk_forward_request.additional_properties = d
        return walk_forward_request

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
