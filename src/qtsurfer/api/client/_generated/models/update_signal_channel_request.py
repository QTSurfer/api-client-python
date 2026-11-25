from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.update_signal_channel_request_visibility import UpdateSignalChannelRequestVisibility
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateSignalChannelRequest")


@_attrs_define
class UpdateSignalChannelRequest:
    """
    Attributes:
        name (str | Unset):
        description (str | Unset):
        visibility (UpdateSignalChannelRequestVisibility | Unset):
        rotate_webhook (bool | Unset): `true` replaces `webhookUrl` with a new address; the old one stops publishing at
            once.
    """

    name: str | Unset = UNSET
    description: str | Unset = UNSET
    visibility: UpdateSignalChannelRequestVisibility | Unset = UNSET
    rotate_webhook: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        visibility: str | Unset = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.value

        rotate_webhook = self.rotate_webhook

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if rotate_webhook is not UNSET:
            field_dict["rotateWebhook"] = rotate_webhook

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _visibility = d.pop("visibility", UNSET)
        visibility: UpdateSignalChannelRequestVisibility | Unset
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = UpdateSignalChannelRequestVisibility(_visibility)

        rotate_webhook = d.pop("rotateWebhook", UNSET)

        update_signal_channel_request = cls(
            name=name,
            description=description,
            visibility=visibility,
            rotate_webhook=rotate_webhook,
        )

        return update_signal_channel_request
