from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LiveSignalInstrument")


@_attrs_define
class LiveSignalInstrument:
    """
    Attributes:
        exchange (str | Unset):
        segment (str | Unset):
        symbol (str | Unset): Slashed form, e.g. `BTC/USDT`.
    """

    exchange: str | Unset = UNSET
    segment: str | Unset = UNSET
    symbol: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exchange = self.exchange

        segment = self.segment

        symbol = self.symbol

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exchange is not UNSET:
            field_dict["exchange"] = exchange
        if segment is not UNSET:
            field_dict["segment"] = segment
        if symbol is not UNSET:
            field_dict["symbol"] = symbol

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        exchange = d.pop("exchange", UNSET)

        segment = d.pop("segment", UNSET)

        symbol = d.pop("symbol", UNSET)

        live_signal_instrument = cls(
            exchange=exchange,
            segment=segment,
            symbol=symbol,
        )

        live_signal_instrument.additional_properties = d
        return live_signal_instrument

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
