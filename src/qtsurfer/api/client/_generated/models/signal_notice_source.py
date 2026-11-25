from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.signal_notice_source_venue_type import SignalNoticeSourceVenueType

T = TypeVar("T", bound="SignalNoticeSource")


@_attrs_define
class SignalNoticeSource:
    """The instrument a notice is about: `LiveSourceRequest` without `type`, which is the subscription's to say, and with
    the instruments named one by one.

        Attributes:
            venue_type (SignalNoticeSourceVenueType):
            exchange (str): As in `LiveSourceRequest`.
            segment (str): As in `LiveSourceRequest`.
            instruments (list[str]): For a `cex` source, 1 to 10 pairs written `BASE/QUOTE`, with no `*`. For a `dex`
                source, exactly one entry, the address of the pool or, on `solana`, the mint of the token (case-sensitive).
    """

    venue_type: SignalNoticeSourceVenueType
    exchange: str
    segment: str
    instruments: list[str]

    def to_dict(self) -> dict[str, Any]:
        venue_type = self.venue_type.value

        exchange = self.exchange

        segment = self.segment

        instruments = self.instruments

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "venueType": venue_type,
                "exchange": exchange,
                "segment": segment,
                "instruments": instruments,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        venue_type = SignalNoticeSourceVenueType(d.pop("venueType"))

        exchange = d.pop("exchange")

        segment = d.pop("segment")

        instruments = cast(list[str], d.pop("instruments"))

        signal_notice_source = cls(
            venue_type=venue_type,
            exchange=exchange,
            segment=segment,
            instruments=instruments,
        )

        return signal_notice_source
