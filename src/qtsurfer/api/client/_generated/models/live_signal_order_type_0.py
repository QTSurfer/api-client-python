from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LiveSignalOrderType0")


@_attrs_define
class LiveSignalOrderType0:
    """Present only for a `hint`.

    Attributes:
        order_kind (str | Unset):
        price (None | str | Unset):
        amount (None | str | Unset):
        stop_price (None | str | Unset):
        trail_pct (None | str | Unset):
    """

    order_kind: str | Unset = UNSET
    price: None | str | Unset = UNSET
    amount: None | str | Unset = UNSET
    stop_price: None | str | Unset = UNSET
    trail_pct: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_kind = self.order_kind

        price: None | str | Unset
        if isinstance(self.price, Unset):
            price = UNSET
        else:
            price = self.price

        amount: None | str | Unset
        if isinstance(self.amount, Unset):
            amount = UNSET
        else:
            amount = self.amount

        stop_price: None | str | Unset
        if isinstance(self.stop_price, Unset):
            stop_price = UNSET
        else:
            stop_price = self.stop_price

        trail_pct: None | str | Unset
        if isinstance(self.trail_pct, Unset):
            trail_pct = UNSET
        else:
            trail_pct = self.trail_pct

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order_kind is not UNSET:
            field_dict["orderKind"] = order_kind
        if price is not UNSET:
            field_dict["price"] = price
        if amount is not UNSET:
            field_dict["amount"] = amount
        if stop_price is not UNSET:
            field_dict["stopPrice"] = stop_price
        if trail_pct is not UNSET:
            field_dict["trailPct"] = trail_pct

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        order_kind = d.pop("orderKind", UNSET)

        def _parse_price(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        price = _parse_price(d.pop("price", UNSET))

        def _parse_amount(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        amount = _parse_amount(d.pop("amount", UNSET))

        def _parse_stop_price(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stop_price = _parse_stop_price(d.pop("stopPrice", UNSET))

        def _parse_trail_pct(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trail_pct = _parse_trail_pct(d.pop("trailPct", UNSET))

        live_signal_order_type_0 = cls(
            order_kind=order_kind,
            price=price,
            amount=amount,
            stop_price=stop_price,
            trail_pct=trail_pct,
        )

        live_signal_order_type_0.additional_properties = d
        return live_signal_order_type_0

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
