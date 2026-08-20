from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="StrategySummary")


@_attrs_define
class StrategySummary:
    """One entry from `GET /strategies` — the same provenance a full `StrategyState` carries
    (`compiledAt`, `requiredSources`), without its validation state, so listing stays cheap
    regardless of how many strategies you have registered. Check a specific strategy's
    validation with `GET /strategy/{strategyId}`.

        Attributes:
            strategy_id (str): Unique identifier for a compiled strategy, derived from the source itself: the same code
                always yields the same id, for every caller, whatever its formatting. See
                `POST /strategy` for exactly which rewrites preserve it and which do not.
                 Example: 6bsh31ikwkuivhtgcoa6s4.
            compiled_at (datetime.datetime | Unset): When the live compilation was produced.
            required_sources (list[str] | Unset): The market data this strategy needs. Absent, not empty, when it could
                not be established without constructing the strategy.
    """

    strategy_id: str
    compiled_at: datetime.datetime | Unset = UNSET
    required_sources: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        strategy_id = self.strategy_id

        compiled_at: str | Unset = UNSET
        if not isinstance(self.compiled_at, Unset):
            compiled_at = self.compiled_at.isoformat()

        required_sources: list[str] | Unset = UNSET
        if not isinstance(self.required_sources, Unset):
            required_sources = self.required_sources

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "strategyId": strategy_id,
            }
        )
        if compiled_at is not UNSET:
            field_dict["compiledAt"] = compiled_at
        if required_sources is not UNSET:
            field_dict["requiredSources"] = required_sources

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        strategy_id = d.pop("strategyId")

        _compiled_at = d.pop("compiledAt", UNSET)
        compiled_at: datetime.datetime | Unset
        if isinstance(_compiled_at, Unset):
            compiled_at = UNSET
        else:
            compiled_at = isoparse(_compiled_at)

        required_sources = cast(list[str], d.pop("requiredSources", UNSET))

        strategy_summary = cls(
            strategy_id=strategy_id,
            compiled_at=compiled_at,
            required_sources=required_sources,
        )

        strategy_summary.additional_properties = d
        return strategy_summary

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
