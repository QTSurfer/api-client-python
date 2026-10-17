from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.live_source_type import LiveSourceType
from ..models.live_source_venue_type import LiveSourceVenueType

T = TypeVar("T", bound="LiveSource")


@_attrs_define
class LiveSource:
    """One market feed a live run consumes. Exactly one entry per run today.

    Attributes:
        venue_type (LiveSourceVenueType): Venue category. `cex` is a centralized exchange and `dex` is one pool on a
            decentralized exchange, which takes its own `exchange`, `segment`, `type` and `instruments` (see "Sources" in
            the Live execution guide). `cx` and `dx`, the spellings used before, are still read as `cex` and `dex`; the run
            always reports the new ones. Example: cex.
        exchange (str): The exchange id, as `GET /exchanges` lists it. For a `dex` source, the chain the pool is on;
            `robinhood` is the only one today. Example: binance.
        segment (str): The segment, as `GET /exchanges` lists it for that exchange, among its `liveSegments` (a segment
            with no live data is refused with `400`). For a `cex` source, the market segment (`spot` today); for a `dex`
            source, the protocol of the pool, `uniswap-v3` the only one today. Example: spot.
        type_ (LiveSourceType): Both `ticker` and `kline` connect to the lightest (fastest) cadence available for the
            exchange — today, 1 tick/second on every supported exchange. Choosing a specific cadence is not offered yet. A
            `dex` source supports only `kline`: one candle per second of the pool's trades.
        instruments (list[str]): The instruments the run reads. For a run started with a list, that list as sent; for
            one started without `instruments`, or with `["*"]`, what the start resolved: the list of pairs the compilation
            of the strategy records as the instruments it accepts, when it records one, or `["*"]` for every instrument the
            exchange/segment offers (tier-gated). An entry is written `BASE/QUOTE` and either side can be `*` to mean any,
            such as any base paired with USDT. Symbols are not case-sensitive and spaces around them are ignored, so
            `btc/usdt` and `BTC/USDT` are the same instrument. A `dex` source holds exactly one entry, the address of its
            pool. Example: ['BTC/USDT'].
    """

    venue_type: LiveSourceVenueType
    exchange: str
    segment: str
    type_: LiveSourceType
    instruments: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        venue_type = self.venue_type.value

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
        venue_type = LiveSourceVenueType(d.pop("venueType"))

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
