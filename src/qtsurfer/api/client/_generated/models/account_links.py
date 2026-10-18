from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.hal_link import HalLink


T = TypeVar("T", bound="AccountLinks")


@_attrs_define
class AccountLinks:
    """HAL `_links` for `GET /account`

    Attributes:
        self_ (HalLink): A HAL link object (Hypertext Application Language)
        usage (HalLink): A HAL link object (Hypertext Application Language)
    """

    self_: HalLink
    usage: HalLink
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_ = self.self_.to_dict()

        usage = self.usage.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "self": self_,
                "usage": usage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hal_link import HalLink

        d = dict(src_dict)
        self_ = HalLink.from_dict(d.pop("self"))

        usage = HalLink.from_dict(d.pop("usage"))

        account_links = cls(
            self_=self_,
            usage=usage,
        )

        account_links.additional_properties = d
        return account_links

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
