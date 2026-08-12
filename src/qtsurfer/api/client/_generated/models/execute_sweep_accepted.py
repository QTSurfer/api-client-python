from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.walk_forward_accepted import WalkForwardAccepted


T = TypeVar("T", bound="ExecuteSweepAccepted")


@_attrs_define
class ExecuteSweepAccepted:
    """
    Attributes:
        sweep_id (str):  Example: swp_95e47a7f0966ce11.
        request_id (str):
        total_runs (int):
        shards (int):
        seed (int): Effective seed used to expand the sweep.
        queued (bool): False when an identical sweep already exists and was not enqueued again.
        walk_forward (WalkForwardAccepted | Unset): Echo of the accepted walk-forward configuration, present only when
            the submit carried one. `inSamplePct` is the resolved value, so a request that omitted it can see what it got.
    """

    sweep_id: str
    request_id: str
    total_runs: int
    shards: int
    seed: int
    queued: bool
    walk_forward: WalkForwardAccepted | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sweep_id = self.sweep_id

        request_id = self.request_id

        total_runs = self.total_runs

        shards = self.shards

        seed = self.seed

        queued = self.queued

        walk_forward: dict[str, Any] | Unset = UNSET
        if not isinstance(self.walk_forward, Unset):
            walk_forward = self.walk_forward.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sweepId": sweep_id,
                "requestId": request_id,
                "totalRuns": total_runs,
                "shards": shards,
                "seed": seed,
                "queued": queued,
            }
        )
        if walk_forward is not UNSET:
            field_dict["walkForward"] = walk_forward

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.walk_forward_accepted import WalkForwardAccepted

        d = dict(src_dict)
        sweep_id = d.pop("sweepId")

        request_id = d.pop("requestId")

        total_runs = d.pop("totalRuns")

        shards = d.pop("shards")

        seed = d.pop("seed")

        queued = d.pop("queued")

        _walk_forward = d.pop("walkForward", UNSET)
        walk_forward: WalkForwardAccepted | Unset
        if isinstance(_walk_forward, Unset):
            walk_forward = UNSET
        else:
            walk_forward = WalkForwardAccepted.from_dict(_walk_forward)

        execute_sweep_accepted = cls(
            sweep_id=sweep_id,
            request_id=request_id,
            total_runs=total_runs,
            shards=shards,
            seed=seed,
            queued=queued,
            walk_forward=walk_forward,
        )

        execute_sweep_accepted.additional_properties = d
        return execute_sweep_accepted

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
