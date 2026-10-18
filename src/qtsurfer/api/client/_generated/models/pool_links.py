from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.hal_link import HalLink


T = TypeVar("T", bound="PoolLinks")


@_attrs_define
class PoolLinks:
    """HAL `_links` — protocol discovery for the pools listing of a decentralized exchange

    Attributes:
        self_ (HalLink): A HAL link object (Hypertext Application Language)
    """

    self_: HalLink
    additional_properties: dict[str, HalLink] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_ = self.self_.to_dict()

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update(
            {
                "self": self_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hal_link import HalLink

        d = dict(src_dict)
        self_ = HalLink.from_dict(d.pop("self"))

        pool_links = cls(
            self_=self_,
        )

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = HalLink.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        pool_links.additional_properties = additional_properties
        return pool_links

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> HalLink:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: HalLink) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
