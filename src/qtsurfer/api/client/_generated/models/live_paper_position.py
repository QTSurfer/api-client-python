from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LivePaperPosition")


@_attrs_define
class LivePaperPosition:
    """
    Attributes:
        instrument (str):  Example: BTC/USDT.
        base (float): Amount held, in the base asset.
        cost (float): What it cost, in the account's currency.
    """

    instrument: str
    base: float
    cost: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instrument = self.instrument

        base = self.base

        cost = self.cost

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "instrument": instrument,
                "base": base,
                "cost": cost,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        instrument = d.pop("instrument")

        base = d.pop("base")

        cost = d.pop("cost")

        live_paper_position = cls(
            instrument=instrument,
            base=base,
            cost=cost,
        )

        live_paper_position.additional_properties = d
        return live_paper_position

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
