from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LivePaperInstrumentOpenPosition")


@_attrs_define
class LivePaperInstrumentOpenPosition:
    """What it holds now. Absent when it holds nothing.

    Attributes:
        base (float): Amount held, in the base asset.
        cost (float): What it cost, in the account's currency.
        mark_price (float | Unset): The price it was valued at in the last mark. Present, with `markedAtMs` and
            `unrealisedPnl`, only when that mark is of the position as it stands now.
        marked_at_ms (int | Unset): Market time (epoch ms) of that mark.
        unrealised_pnl (float | Unset): `base` times `markPrice`, minus `cost`, in the account's currency.
    """

    base: float
    cost: float
    mark_price: float | Unset = UNSET
    marked_at_ms: int | Unset = UNSET
    unrealised_pnl: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base = self.base

        cost = self.cost

        mark_price = self.mark_price

        marked_at_ms = self.marked_at_ms

        unrealised_pnl = self.unrealised_pnl

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "base": base,
                "cost": cost,
            }
        )
        if mark_price is not UNSET:
            field_dict["markPrice"] = mark_price
        if marked_at_ms is not UNSET:
            field_dict["markedAtMs"] = marked_at_ms
        if unrealised_pnl is not UNSET:
            field_dict["unrealisedPnl"] = unrealised_pnl

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        base = d.pop("base")

        cost = d.pop("cost")

        mark_price = d.pop("markPrice", UNSET)

        marked_at_ms = d.pop("markedAtMs", UNSET)

        unrealised_pnl = d.pop("unrealisedPnl", UNSET)

        live_paper_instrument_open_position = cls(
            base=base,
            cost=cost,
            mark_price=mark_price,
            marked_at_ms=marked_at_ms,
            unrealised_pnl=unrealised_pnl,
        )

        live_paper_instrument_open_position.additional_properties = d
        return live_paper_instrument_open_position

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
