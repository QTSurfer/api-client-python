from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.live_source_request_type import LiveSourceRequestType
from ..types import UNSET, Unset

T = TypeVar("T", bound="LiveSourceRequest")


@_attrs_define
class LiveSourceRequest:
    """One market feed to start a live run on. Exactly one entry per run today. It is `LiveSource` as you ask for it: the
    only difference is that `instruments` can be left out.

        Attributes:
            venue_type (str): Venue category. `cx` (centralized exchange) is the only one live runs support today. Example:
                cx.
            exchange (str):  Example: binance.
            segment (str):  Example: spot.
            type_ (LiveSourceRequestType): Both `ticker` and `kline` connect to the lightest (fastest) cadence available for
                the exchange — today, 1 tick/second on every supported exchange. Choosing a specific cadence is not offered yet.
            instruments (list[str] | Unset): Which instruments the run reads. A QTScript strategy can declare which
                instruments it accepts with an `instruments` line in its source. When the compilation of the strategy records
                that selection as a list of pairs, leaving `instruments` out, or sending `["*"]`, takes that list; otherwise the
                run reads every instrument the exchange/segment offers. A list of instruments is taken as sent, and `[]` and
                `null` are refused with `400`. An entry is written `BASE/QUOTE`; either side can be `*` to mean any: any base
                can be paired with USDT, and BTC can be paired with any quote. Entries are not case-sensitive and spaces around
                them are ignored, so `btc/usdt` and `BTC/USDT` are the same instrument. An entry that is not of that form (no
                `/`, an empty side, a `.` or a space inside a side, or a `*` mixed with other characters of a side) makes the
                run fail when it starts. Plan limits: a list with an entry that has a `*` on a side counts like `["*"]` and only
                plans that include the wildcard accept it; the other entries are counted one by one. The instruments the run
                actually reads come back in the run's `sources`. Example: ['BTC/USDT'].
    """

    venue_type: str
    exchange: str
    segment: str
    type_: LiveSourceRequestType
    instruments: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        venue_type = self.venue_type

        exchange = self.exchange

        segment = self.segment

        type_ = self.type_.value

        instruments: list[str] | Unset = UNSET
        if not isinstance(self.instruments, Unset):
            instruments = self.instruments

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "venueType": venue_type,
                "exchange": exchange,
                "segment": segment,
                "type": type_,
            }
        )
        if instruments is not UNSET:
            field_dict["instruments"] = instruments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        venue_type = d.pop("venueType")

        exchange = d.pop("exchange")

        segment = d.pop("segment")

        type_ = LiveSourceRequestType(d.pop("type"))

        instruments = cast(list[str], d.pop("instruments", UNSET))

        live_source_request = cls(
            venue_type=venue_type,
            exchange=exchange,
            segment=segment,
            type_=type_,
            instruments=instruments,
        )

        live_source_request.additional_properties = d
        return live_source_request

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
