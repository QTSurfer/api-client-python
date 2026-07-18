from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SweepProgress")


@_attrs_define
class SweepProgress:
    """
    Attributes:
        done (int):
        total (int):
        aborted (int):
        shard_count (int):
        pending_shards (int):
    """

    done: int
    total: int
    aborted: int
    shard_count: int
    pending_shards: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        done = self.done

        total = self.total

        aborted = self.aborted

        shard_count = self.shard_count

        pending_shards = self.pending_shards

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "done": done,
                "total": total,
                "aborted": aborted,
                "shardCount": shard_count,
                "pendingShards": pending_shards,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        done = d.pop("done")

        total = d.pop("total")

        aborted = d.pop("aborted")

        shard_count = d.pop("shardCount")

        pending_shards = d.pop("pendingShards")

        sweep_progress = cls(
            done=done,
            total=total,
            aborted=aborted,
            shard_count=shard_count,
            pending_shards=pending_shards,
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
