from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LiveRunStats")


@_attrs_define
class LiveRunStats:
    """What a run has been doing, as of its last snapshot. The platform refreshes it about once a minute
    while the run is being executed, so `opsPerSecond` is an average over that interval, not an
    instantaneous rate.

        Attributes:
            processed (int): Updates of instruments the run has accepted since it started executing. It can start again from
                zero if the run is restarted.
            ops_per_second (float): Updates accepted per second over the last refresh interval. `0` when none arrived.
            instruments_seen (int): How many distinct instruments the run has received an update for.
            as_of_ms (int): Epoch milliseconds when these counters were last written.
            stale (bool): `true` when the run is meant to be running (`desired` is `RUNNING`) and its counters have not
                been refreshed for several refresh intervals: the platform has stopped updating them, which is
                worth checking against `state`. `false` otherwise. A run whose `processed` is flat is not stale;
                `progressedAtMs` is how to tell it apart.
            progressed_at_ms (int | Unset): Epoch milliseconds of the last snapshot in which `processed` had grown. Absent
                until the run has
                processed anything. A run fed by a source that updates rarely (a funding rate, for example) can
                stay flat for hours: that is how such a run behaves, not a fault.
    """

    processed: int
    ops_per_second: float
    instruments_seen: int
    as_of_ms: int
    stale: bool
    progressed_at_ms: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        processed = self.processed

        ops_per_second = self.ops_per_second

        instruments_seen = self.instruments_seen

        as_of_ms = self.as_of_ms

        stale = self.stale

        progressed_at_ms = self.progressed_at_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "processed": processed,
                "opsPerSecond": ops_per_second,
                "instrumentsSeen": instruments_seen,
                "asOfMs": as_of_ms,
                "stale": stale,
            }
        )
        if progressed_at_ms is not UNSET:
            field_dict["progressedAtMs"] = progressed_at_ms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        processed = d.pop("processed")

        ops_per_second = d.pop("opsPerSecond")

        instruments_seen = d.pop("instrumentsSeen")

        as_of_ms = d.pop("asOfMs")

        stale = d.pop("stale")

        progressed_at_ms = d.pop("progressedAtMs", UNSET)

        live_run_stats = cls(
            processed=processed,
            ops_per_second=ops_per_second,
            instruments_seen=instruments_seen,
            as_of_ms=as_of_ms,
            stale=stale,
            progressed_at_ms=progressed_at_ms,
        )

        live_run_stats.additional_properties = d
        return live_run_stats

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
