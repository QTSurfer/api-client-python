from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.public_live_list_links import PublicLiveListLinks
    from ..models.signal_channel import SignalChannel


T = TypeVar("T", bound="PublicSignalChannelPage")


@_attrs_define
class PublicSignalChannelPage:
    """
    Attributes:
        channels (list[SignalChannel]):
        field_links (PublicLiveListLinks | Unset): Present only when another page exists.
    """

    channels: list[SignalChannel]
    field_links: PublicLiveListLinks | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channels = []
        for channels_item_data in self.channels:
            channels_item = channels_item_data.to_dict()
            channels.append(channels_item)

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "channels": channels,
            }
        )
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.public_live_list_links import PublicLiveListLinks
        from ..models.signal_channel import SignalChannel

        d = dict(src_dict)
        channels = []
        _channels = d.pop("channels")
        for channels_item_data in _channels:
            channels_item = SignalChannel.from_dict(channels_item_data)

            channels.append(channels_item)

        _field_links = d.pop("_links", UNSET)
        field_links: PublicLiveListLinks | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = PublicLiveListLinks.from_dict(_field_links)

        public_signal_channel_page = cls(
            channels=channels,
            field_links=field_links,
        )

        public_signal_channel_page.additional_properties = d
        return public_signal_channel_page

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
