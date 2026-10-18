from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.send_live_command_request_properties import SendLiveCommandRequestProperties


T = TypeVar("T", bound="SendLiveCommandRequest")


@_attrs_define
class SendLiveCommandRequest:
    """
    Attributes:
        command (str): The command's text — non-blank.
        properties (SendLiveCommandRequestProperties | Unset): An optional map of your own choosing, alongside command.
            Absent means none; when given, it must be a JSON object, and `command` and `properties` are the only keys the
            body may carry. Each entry lands as a top-level entry on the strategy's `CommandRequest` — no key is off limits,
            since the command's own text is kept separately.
    """

    command: str
    properties: SendLiveCommandRequestProperties | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        command = self.command

        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "command": command,
            }
        )
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.send_live_command_request_properties import SendLiveCommandRequestProperties

        d = dict(src_dict)
        command = d.pop("command")

        _properties = d.pop("properties", UNSET)
        properties: SendLiveCommandRequestProperties | Unset
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = SendLiveCommandRequestProperties.from_dict(_properties)

        send_live_command_request = cls(
            command=command,
            properties=properties,
        )

        send_live_command_request.additional_properties = d
        return send_live_command_request

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
