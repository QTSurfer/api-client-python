from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.public_live_next_link import PublicLiveNextLink


T = TypeVar("T", bound="PublicLiveListLinks")


@_attrs_define
class PublicLiveListLinks:
    """Present only when another page exists.

    Attributes:
        next_ (PublicLiveNextLink | Unset):
    """

    next_: PublicLiveNextLink | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        next_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.next_, Unset):
            next_ = self.next_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if next_ is not UNSET:
            field_dict["next"] = next_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.public_live_next_link import PublicLiveNextLink

        d = dict(src_dict)
        _next_ = d.pop("next", UNSET)
        next_: PublicLiveNextLink | Unset
        if isinstance(_next_, Unset):
            next_ = UNSET
        else:
            next_ = PublicLiveNextLink.from_dict(_next_)

        public_live_list_links = cls(
            next_=next_,
        )

        public_live_list_links.additional_properties = d
        return public_live_list_links

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
