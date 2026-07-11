from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HalLink")


@_attrs_define
class HalLink:
    """A HAL link object (Hypertext Application Language)

    Attributes:
        href (str): The link target as an absolute-path URI reference (resolve against the API base). A URI Template
            (RFC 6570) when `templated` is true. Example: /v1/exchange/binance/spot/instruments.
        templated (bool | Unset): True when `href` is an RFC 6570 URI Template.
    """

    href: str
    templated: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        href = self.href

        templated = self.templated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "href": href,
            }
        )
        if templated is not UNSET:
            field_dict["templated"] = templated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        href = d.pop("href")

        templated = d.pop("templated", UNSET)

        hal_link = cls(
            href=href,
            templated=templated,
        )

        hal_link.additional_properties = d
        return hal_link

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
