from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pool_detail import PoolDetail
    from ..models.pool_links import PoolLinks
    from ..models.pool_list_meta import PoolListMeta


T = TypeVar("T", bound="PoolListResponse")


@_attrs_define
class PoolListResponse:
    """HAL-style response envelope for the instruments listing of a decentralized exchange, whose instruments are pools

    Example:
        {'data': [{'id': '0x52e65b17fb6e5ba00ed806f37afcd2daa50271ca', 'symbol': 'WETH/USDG', 'base': 'WETH', 'quote':
            'USDG', 'baseAddress': '0x0bd7d308f8e1639fab988df18a8011f41eacad73', 'quoteAddress':
            '0x5fc5360d0400a0fd4f2af552add042d716f1d168', 'feePercent': 0.01, 'lastPrice': 2411.285967, 'volume24h':
            274033077.4, 'tvlUsd': 19857902.02, 'volume24hUsd': 273876056.45, 'createdAt': '2026-07-02T20:51:08Z'}], 'meta':
            {'updatedAt': '2026-10-14T22:32:34Z', 'exchange': 'robinhood', 'segment': 'uniswap-v3', 'venueType': 'dex',
            'minTvlUsd': 10000, 'limit': 50}, '_links': {'self': {'href': '/v1/exchange/robinhood/uniswap-v3/instruments'},
            'uniswap-v3': {'href': '/v1/exchange/robinhood/uniswap-v3/instruments'}}}

    Attributes:
        data (list[PoolDetail]): The pools worth running, the most traded in the last 24 hours first
        meta (PoolListMeta): Metadata describing the pools listing of a decentralized exchange
        field_links (PoolLinks): HAL `_links` — protocol discovery for the pools listing of a decentralized exchange
    """

    data: list[PoolDetail]
    meta: PoolListMeta
    field_links: PoolLinks
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        meta = self.meta.to_dict()

        field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "meta": meta,
                "_links": field_links,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pool_detail import PoolDetail
        from ..models.pool_links import PoolLinks
        from ..models.pool_list_meta import PoolListMeta

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = PoolDetail.from_dict(data_item_data)

            data.append(data_item)

        meta = PoolListMeta.from_dict(d.pop("meta"))

        field_links = PoolLinks.from_dict(d.pop("_links"))

        pool_list_response = cls(
            data=data,
            meta=meta,
            field_links=field_links,
        )

        pool_list_response.additional_properties = d
        return pool_list_response

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
