from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.live_paper_equity_point_kind import LivePaperEquityPointKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="LivePaperEquityPoint")


@_attrs_define
class LivePaperEquityPoint:
    """
    Attributes:
        currency (str):
        kind (LivePaperEquityPointKind):
        event_ts_ms (int): Market time of the point.
        equity (float | Unset): Absent on a `gap`.
    """

    currency: str
    kind: LivePaperEquityPointKind
    event_ts_ms: int
    equity: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency = self.currency

        kind = self.kind.value

        event_ts_ms = self.event_ts_ms

        equity = self.equity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currency": currency,
                "kind": kind,
                "eventTsMs": event_ts_ms,
            }
        )
        if equity is not UNSET:
            field_dict["equity"] = equity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        currency = d.pop("currency")

        kind = LivePaperEquityPointKind(d.pop("kind"))

        event_ts_ms = d.pop("eventTsMs")

        equity = d.pop("equity", UNSET)

        live_paper_equity_point = cls(
            currency=currency,
            kind=kind,
            event_ts_ms=event_ts_ms,
            equity=equity,
        )

        live_paper_equity_point.additional_properties = d
        return live_paper_equity_point

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
