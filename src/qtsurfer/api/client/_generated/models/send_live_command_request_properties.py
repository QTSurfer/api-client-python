from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SendLiveCommandRequestProperties")


@_attrs_define
class SendLiveCommandRequestProperties:
    """An optional map of your own choosing, alongside command. Absent means none; when given, it must be a JSON object,
    and `command` and `properties` are the only keys the body may carry. Each entry lands as a top-level entry on the
    strategy's `CommandRequest` — no key is off limits, since the command's own text is kept separately.

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        send_live_command_request_properties = cls()

        send_live_command_request_properties.additional_properties = d
        return send_live_command_request_properties

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
