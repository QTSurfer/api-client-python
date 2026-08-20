from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.hal_link import HalLink


T = TypeVar("T", bound="StrategyLinks")


@_attrs_define
class StrategyLinks:
    """HAL `_links` for a strategy — present on a full `StrategyState` body (`GET
    /strategy/{strategyId}`, and `POST /strategy/{strategyId}/validate`'s already-validated
    `200`), absent from that same endpoint's `202` — a deliberately partial stub carrying only
    what is known before a check has even started. Following `code` can still `404` once
    present: it documents its own honest "nothing to return" for a strategy with no source of
    its own (a `REFERENCE` marketplace copy, or one resolved only through the platform's shared
    pool). This link says where to look, not that something is there.

        Attributes:
            code (HalLink): A HAL link object (Hypertext Application Language)
    """

    code: HalLink
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hal_link import HalLink

        d = dict(src_dict)
        code = HalLink.from_dict(d.pop("code"))

        strategy_links = cls(
            code=code,
        )

        strategy_links.additional_properties = d
        return strategy_links

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
