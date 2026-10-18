from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.pool_list_meta_venue_type import PoolListMetaVenueType

T = TypeVar("T", bound="PoolListMeta")


@_attrs_define
class PoolListMeta:
    """Metadata describing the pools listing of a decentralized exchange

    Attributes:
        updated_at (datetime.datetime): When this listing was last refreshed. It is refreshed every hour, and the
            `lastPrice` of each pool is as of this time. Example: 2026-10-14T22:32:34Z.
        exchange (str): The exchange the pools belong to Example: robinhood.
        segment (str): The protocol served in `data`, one of the exchange's `segments` Example: uniswap-v3.
        venue_type (PoolListMetaVenueType): The venue type of the exchange, as `GET /exchanges` lists it. Always `dex`
            here; a listing of instruments of a centralized exchange says `cex`. Example: dex.
        min_tvl_usd (float): A pool with less liquidity than this (in US dollars) is not listed Example: 10000.
        limit (int): The most pools the listing has Example: 50.
    """

    updated_at: datetime.datetime
    exchange: str
    segment: str
    venue_type: PoolListMetaVenueType
    min_tvl_usd: float
    limit: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        updated_at = self.updated_at.isoformat()

        exchange = self.exchange

        segment = self.segment

        venue_type = self.venue_type.value

        min_tvl_usd = self.min_tvl_usd

        limit = self.limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "updatedAt": updated_at,
                "exchange": exchange,
                "segment": segment,
                "venueType": venue_type,
                "minTvlUsd": min_tvl_usd,
                "limit": limit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        updated_at = isoparse(d.pop("updatedAt"))

        exchange = d.pop("exchange")

        segment = d.pop("segment")

        venue_type = PoolListMetaVenueType(d.pop("venueType"))

        min_tvl_usd = d.pop("minTvlUsd")

        limit = d.pop("limit")

        pool_list_meta = cls(
            updated_at=updated_at,
            exchange=exchange,
            segment=segment,
            venue_type=venue_type,
            min_tvl_usd=min_tvl_usd,
            limit=limit,
        )

        pool_list_meta.additional_properties = d
        return pool_list_meta

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
