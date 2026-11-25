from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.signal_channel_request_visibility import SignalChannelRequestVisibility
from ..types import UNSET, Unset

T = TypeVar("T", bound="SignalChannelRequest")


@_attrs_define
class SignalChannelRequest:
    """
    Attributes:
        name (str): The name subscribers see. Your own user is never shown.
        description (str | Unset):
        visibility (SignalChannelRequestVisibility | Unset): `unlisted`: found only by its `channelId`. `public`: also
            listed in `GET /signals/channels/public`. Default: SignalChannelRequestVisibility.UNLISTED.
    """

    name: str
    description: str | Unset = UNSET
    visibility: SignalChannelRequestVisibility | Unset = SignalChannelRequestVisibility.UNLISTED

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        visibility: str | Unset = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if visibility is not UNSET:
            field_dict["visibility"] = visibility

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description", UNSET)

        _visibility = d.pop("visibility", UNSET)
        visibility: SignalChannelRequestVisibility | Unset
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = SignalChannelRequestVisibility(_visibility)

        signal_channel_request = cls(
            name=name,
            description=description,
            visibility=visibility,
        )

        return signal_channel_request
