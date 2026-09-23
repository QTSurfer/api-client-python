from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.live_source_type import LiveSourceType

T = TypeVar("T", bound="LiveSource")


@_attrs_define
class LiveSource:
    """One market feed a live run consumes. Exactly one entry per run today.

    Attributes:
        venue_type (str): Venue category. `cx` (centralized exchange) is the only one live runs support today. Example:
            cx.
        exchange (str):  Example: binance.
        segment (str):  Example: spot.
        type_ (LiveSourceType): Both `ticker` and `kline` connect to the lightest (fastest) cadence available for the
            exchange — today, 1 tick/second on every supported exchange. Choosing a specific cadence is not offered yet.
        instruments (list[str]): Instrument symbols, or `["*"]` for every instrument the exchange/segment offers (tier-
            gated). Example: ['BTC/USDT'].
    """

    venue_type: str
    exchange: str
    segment: str
    type_: LiveSourceType
    instruments: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        venue_type = self.venue_type

        exchange = self.exchange

        segment = self.segment

        type_ = self.type_.value

        instruments = self.instruments

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "venueType": venue_type,
                "exchange": exchange,
                "segment": segment,
                "type": type_,
                "instruments": instruments,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        venue_type = d.pop("venueType")

        exchange = d.pop("exchange")

        segment = d.pop("segment")

        type_ = LiveSourceType(d.pop("type"))

        instruments = cast(list[str], d.pop("instruments"))

        live_source = cls(
            venue_type=venue_type,
            exchange=exchange,
            segment=segment,
            type_=type_,
            instruments=instruments,
        )

        live_source.additional_properties = d
        return live_source

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
