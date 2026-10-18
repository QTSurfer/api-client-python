from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EquityPoint")


@_attrs_define
class EquityPoint:
    """Single sample of the running equity at a yield event.

    Attributes:
        timestamp (int): Epoch milliseconds. The first point in an equity curve is anchored at the backtest `from`;
            subsequent points carry the timestamp of each emitted yield. Example: 1700000000000.
        equity (float): Running equity at this point (`initialCapital + cumulativePnl`). Example: 110.5.
    """

    timestamp: int
    equity: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        equity = self.equity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "equity": equity,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        timestamp = d.pop("timestamp")

        equity = d.pop("equity")

        equity_point = cls(
            timestamp=timestamp,
            equity=equity,
        )

        equity_point.additional_properties = d
        return equity_point

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
