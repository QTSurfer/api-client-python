from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.exchange_venue_type import ExchangeVenueType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Exchange")


@_attrs_define
class Exchange:
    """Exchange service provider

    Attributes:
        id (str): Unique identifier for the exchange Example: binance.
        name (str): Name of the exchange Example: Binance.
        venue_type (ExchangeVenueType): Venue category, written as the `venueType` of a live run's source: `cex` is a
            centralized exchange and `dex` a decentralized one. A `dex` exchange has no market data to prepare or backtest,
            so its id is not valid in the routes that take an `exchangeId`, except the two instruments routes, which list
            its pools (the instrument of a run on it is a pool's address). Example: cex.
        segments (list[str]): The segments the exchange offers, written as in the path of `GET
            /exchange/{exchangeId}/{segment}/instruments` and as the `segment` of a live run's source. For a `cex` exchange,
            its market segments (`spot`, `futures`: the ones its instrument catalogues are served under); for a `dex`
            exchange, the protocols whose pools a run can read. Example: ['spot', 'futures'].
        live_segments (list[str]): The segments among `segments` for which live data is published, so the ones a live
            run can read: a live run on any other segment of the exchange is refused with `400`. It can be empty (an
            exchange whose live data is not published yet). Example: ['spot'].
        description (str | Unset): Description of the exchange Example: Binance cryptocurrency exchange.
    """

    id: str
    name: str
    venue_type: ExchangeVenueType
    segments: list[str]
    live_segments: list[str]
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        venue_type = self.venue_type.value

        segments = self.segments

        live_segments = self.live_segments

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "venueType": venue_type,
                "segments": segments,
                "liveSegments": live_segments,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        venue_type = ExchangeVenueType(d.pop("venueType"))

        segments = cast(list[str], d.pop("segments"))

        live_segments = cast(list[str], d.pop("liveSegments"))

        description = d.pop("description", UNSET)

        exchange = cls(
            id=id,
            name=name,
            venue_type=venue_type,
            segments=segments,
            live_segments=live_segments,
            description=description,
        )

        exchange.additional_properties = d
        return exchange

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
