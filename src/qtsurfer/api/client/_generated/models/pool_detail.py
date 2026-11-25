from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PoolDetail")


@_attrs_define
class PoolDetail:
    """A pool of a decentralized exchange. The listing is a place to start, not the whole market: a live run
    can read any pool of the protocol, listed or not, on an exchange whose segment is in `liveSegments`.

        Attributes:
            id (str): The pool's address. On an EVM chain (`robinhood`) it is `0x` and 40 hexadecimal digits, in lower case.
                On `solana` it is a base58 address of 32 to 44 characters, which is case-sensitive: use it exactly as
                listed. It is the value to put in `instruments` of a live run's source.
                 Example: 0x52e65b17fb6e5ba00ed806f37afcd2daa50271ca.
            symbol (str): The pair written `BASE/QUOTE`, the way the signals of a run on this pool name it (`instrument`)
                Example: WETH/USDG.
            base (str): Symbol of the base token Example: WETH.
            quote (str): Symbol of the quote token Example: USDG.
            base_address (str): Address of the base token, in the form of `id` (lower case on an EVM chain; as written,
                base58 and case-sensitive, on `solana`) Example: 0x0bd7d308f8e1639fab988df18a8011f41eacad73.
            quote_address (str): Address of the quote token, in the form of `id` (lower case on an EVM chain; as written,
                base58 and case-sensitive, on `solana`) Example: 0x5fc5360d0400a0fd4f2af552add042d716f1d168.
            tvl_usd (float): The liquidity held by the pool, in US dollars Example: 19857902.02.
            volume_24_h_usd (float): What traded in the pool over the last 24 hours, in US dollars Example: 273876056.45.
            fee_percent (float | Unset): The pool's fee tier, in percent (`0.05` is a 0.05 % fee). A protocol can have
                several pools of the same pair, one per fee tier. Absent when the source does not tell it, which is the case of
                most pools of `solana`. Example: 0.01.
            last_price (float | Unset): The price of one base token in the quote token, as the signals of a run on this pool
                name the pair. It is as of `meta.updatedAt`. Absent when there is no price for the pool. Example: 2411.285967.
            volume24h (float | Unset): What traded in the pool over the last 24 hours, in the quote token, the same meaning
                as `volume24h` of an instrument of a centralized exchange. Absent when the quote token has no dollar price to
                convert from. Example: 274033077.4.
            created_at (datetime.datetime | Unset): When the pool was created. Absent when it is not known Example:
                2026-07-02T20:51:08Z.
    """

    id: str
    symbol: str
    base: str
    quote: str
    base_address: str
    quote_address: str
    tvl_usd: float
    volume_24_h_usd: float
    fee_percent: float | Unset = UNSET
    last_price: float | Unset = UNSET
    volume24h: float | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        symbol = self.symbol

        base = self.base

        quote = self.quote

        base_address = self.base_address

        quote_address = self.quote_address

        tvl_usd = self.tvl_usd

        volume_24_h_usd = self.volume_24_h_usd

        fee_percent = self.fee_percent

        last_price = self.last_price

        volume24h = self.volume24h

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "symbol": symbol,
                "base": base,
                "quote": quote,
                "baseAddress": base_address,
                "quoteAddress": quote_address,
                "tvlUsd": tvl_usd,
                "volume24hUsd": volume_24_h_usd,
            }
        )
        if fee_percent is not UNSET:
            field_dict["feePercent"] = fee_percent
        if last_price is not UNSET:
            field_dict["lastPrice"] = last_price
        if volume24h is not UNSET:
            field_dict["volume24h"] = volume24h
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        symbol = d.pop("symbol")

        base = d.pop("base")

        quote = d.pop("quote")

        base_address = d.pop("baseAddress")

        quote_address = d.pop("quoteAddress")

        tvl_usd = d.pop("tvlUsd")

        volume_24_h_usd = d.pop("volume24hUsd")

        fee_percent = d.pop("feePercent", UNSET)

        last_price = d.pop("lastPrice", UNSET)

        volume24h = d.pop("volume24h", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        pool_detail = cls(
            id=id,
            symbol=symbol,
            base=base,
            quote=quote,
            base_address=base_address,
            quote_address=quote_address,
            tvl_usd=tvl_usd,
            volume_24_h_usd=volume_24_h_usd,
            fee_percent=fee_percent,
            last_price=last_price,
            volume24h=volume24h,
            created_at=created_at,
        )

        pool_detail.additional_properties = d
        return pool_detail

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
