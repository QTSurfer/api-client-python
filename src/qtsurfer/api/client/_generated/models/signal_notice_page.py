from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.public_live_list_links import PublicLiveListLinks
    from ..models.signal_notice import SignalNotice


T = TypeVar("T", bound="SignalNoticePage")


@_attrs_define
class SignalNoticePage:
    """
    Attributes:
        notices (list[SignalNotice]):
        field_links (PublicLiveListLinks | Unset): Present only when another page exists.
    """

    notices: list[SignalNotice]
    field_links: PublicLiveListLinks | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        notices = []
        for notices_item_data in self.notices:
            notices_item = notices_item_data.to_dict()
            notices.append(notices_item)

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "notices": notices,
            }
        )
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.public_live_list_links import PublicLiveListLinks
        from ..models.signal_notice import SignalNotice

        d = dict(src_dict)
        notices = []
        _notices = d.pop("notices")
        for notices_item_data in _notices:
            notices_item = SignalNotice.from_dict(notices_item_data)

            notices.append(notices_item)

        _field_links = d.pop("_links", UNSET)
        field_links: PublicLiveListLinks | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = PublicLiveListLinks.from_dict(_field_links)

        signal_notice_page = cls(
            notices=notices,
            field_links=field_links,
        )

        signal_notice_page.additional_properties = d
        return signal_notice_page

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
