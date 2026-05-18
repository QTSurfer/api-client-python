from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="InstrumentDetail")


@_attrs_define
class InstrumentDetail:
    """Exchange instrument with data availability and market info

    Attributes:
        id (str): Instrument identifier (e.g. currency pair) Example: BTC/USDT.
        base (str): Base currency Example: BTC.
        quote (str): Quote currency Example: USDT.
        data_from (datetime.datetime | Unset): Earliest timestamp with quality-verified data available for backtesting
            Example: 2026-03-17T00:00:00Z.
        data_to (datetime.datetime | Unset): Latest timestamp with quality-verified data available for backtesting
            Example: 2026-03-31T18:00:00Z.
        last_price (float | Unset): Last traded price Example: 84250.5.
        volume24h (float | Unset): Trading volume in the last 24 hours (in quote currency) Example: 1234567.89.
    """

    id: str
    base: str
    quote: str
    data_from: datetime.datetime | Unset = UNSET
    data_to: datetime.datetime | Unset = UNSET
    last_price: float | Unset = UNSET
    volume24h: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        base = self.base

        quote = self.quote

        data_from: str | Unset = UNSET
        if not isinstance(self.data_from, Unset):
            data_from = self.data_from.isoformat()

        data_to: str | Unset = UNSET
        if not isinstance(self.data_to, Unset):
            data_to = self.data_to.isoformat()

        last_price = self.last_price

        volume24h = self.volume24h

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "base": base,
                "quote": quote,
            }
        )
        if data_from is not UNSET:
            field_dict["dataFrom"] = data_from
        if data_to is not UNSET:
            field_dict["dataTo"] = data_to
        if last_price is not UNSET:
            field_dict["lastPrice"] = last_price
        if volume24h is not UNSET:
            field_dict["volume24h"] = volume24h

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        base = d.pop("base")

        quote = d.pop("quote")

        _data_from = d.pop("dataFrom", UNSET)
        data_from: datetime.datetime | Unset
        if isinstance(_data_from, Unset):
            data_from = UNSET
        else:
            data_from = isoparse(_data_from)

        _data_to = d.pop("dataTo", UNSET)
        data_to: datetime.datetime | Unset
        if isinstance(_data_to, Unset):
            data_to = UNSET
        else:
            data_to = isoparse(_data_to)

        last_price = d.pop("lastPrice", UNSET)

        volume24h = d.pop("volume24h", UNSET)

        instrument_detail = cls(
            id=id,
            base=base,
            quote=quote,
            data_from=data_from,
            data_to=data_to,
            last_price=last_price,
            volume24h=volume24h,
        )

        instrument_detail.additional_properties = d
        return instrument_detail

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
