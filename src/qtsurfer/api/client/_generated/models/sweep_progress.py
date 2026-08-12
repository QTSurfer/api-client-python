from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SweepProgress")


@_attrs_define
class SweepProgress:
    """How far along a sweep is, and — when the sweep is still running — enough to tell a healthy one from a stuck one. The
    counts partition the shards (or, for a walk-forward sweep, the folds): every unit is either finished, failed,
    waiting to be retried, or not yet started.

        Attributes:
            done (int):
            total (int):
            aborted (int): Individual runs that executed and aborted. A row-level count: a shard that fails before producing
                any rows leaves this at 0, which is why `failedShards` exists alongside it.
            shard_count (int):
            pending_shards (int):
            failed_shards (int): Shards (or folds) that failed and will not be retried. Distinct from `aborted`: this counts
                whole units that never reported, not runs that ran badly.
            retrying (int): Units whose last attempt failed on something transient — an I/O error, a worker that died mid-
                read — and which are queued to be attempted again. Not counted as failures, because they have not failed yet; a
                sweep with a non-zero value here is still expected to complete.
            not_started (int): Units that have not reported anything yet. Covers both work still queued behind other work
                and work claimed by a worker that stopped before it began, which is why a sweep with a persistent value here and
                a rising `stalledSeconds` is worth looking at.
            stalled_seconds (int | Unset): Seconds since anything last advanced. Omitted on a finished sweep, where it would
                only measure how long ago it finished, and on sweeps submitted before this field existed.
            eta_seconds (int | Unset): Rough seconds remaining, extrapolated from the rate observed so far and assuming
                nothing else competes for workers. Runs conservative in practice — it has measured 2–5× long when a sweep spent
                part of its life waiting to be retried, since that wait dilutes the observed rate. **Omitted, never zero, when
                it cannot be computed**: a sweep with nothing finished yet has no rate to extrapolate from, and a zero would
                read as "about to finish". Excludes queue wait entirely; `retrying` and `stalledSeconds` are where that shows
                up.
    """

    done: int
    total: int
    aborted: int
    shard_count: int
    pending_shards: int
    failed_shards: int
    retrying: int
    not_started: int
    stalled_seconds: int | Unset = UNSET
    eta_seconds: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        done = self.done

        total = self.total

        aborted = self.aborted

        shard_count = self.shard_count

        pending_shards = self.pending_shards

        failed_shards = self.failed_shards

        retrying = self.retrying

        not_started = self.not_started

        stalled_seconds = self.stalled_seconds

        eta_seconds = self.eta_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "done": done,
                "total": total,
                "aborted": aborted,
                "shardCount": shard_count,
                "pendingShards": pending_shards,
                "failedShards": failed_shards,
                "retrying": retrying,
                "notStarted": not_started,
            }
        )
        if stalled_seconds is not UNSET:
            field_dict["stalledSeconds"] = stalled_seconds
        if eta_seconds is not UNSET:
            field_dict["etaSeconds"] = eta_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        done = d.pop("done")

        total = d.pop("total")

        aborted = d.pop("aborted")

        shard_count = d.pop("shardCount")

        pending_shards = d.pop("pendingShards")

        failed_shards = d.pop("failedShards")

        retrying = d.pop("retrying")

        not_started = d.pop("notStarted")

        stalled_seconds = d.pop("stalledSeconds", UNSET)

        eta_seconds = d.pop("etaSeconds", UNSET)

        sweep_progress = cls(
            done=done,
            total=total,
            aborted=aborted,
            shard_count=shard_count,
            pending_shards=pending_shards,
            failed_shards=failed_shards,
            retrying=retrying,
            not_started=not_started,
            stalled_seconds=stalled_seconds,
            eta_seconds=eta_seconds,
        )

        sweep_progress.additional_properties = d
        return sweep_progress

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
