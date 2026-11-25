from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SignalNoticeAccepted")


@_attrs_define
class SignalNoticeAccepted:
    """
    Attributes:
        notice_id (str):
        deliveries (int): How many subscriptions the notice goes to.
        received_at_ms (int):
        expires_at_ms (int):
    """

    notice_id: str
    deliveries: int
    received_at_ms: int
    expires_at_ms: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        notice_id = self.notice_id

        deliveries = self.deliveries

        received_at_ms = self.received_at_ms

        expires_at_ms = self.expires_at_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "noticeId": notice_id,
                "deliveries": deliveries,
                "receivedAtMs": received_at_ms,
                "expiresAtMs": expires_at_ms,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        notice_id = d.pop("noticeId")

        deliveries = d.pop("deliveries")

        received_at_ms = d.pop("receivedAtMs")

        expires_at_ms = d.pop("expiresAtMs")

        signal_notice_accepted = cls(
            notice_id=notice_id,
            deliveries=deliveries,
            received_at_ms=received_at_ms,
            expires_at_ms=expires_at_ms,
        )

        signal_notice_accepted.additional_properties = d
        return signal_notice_accepted

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
