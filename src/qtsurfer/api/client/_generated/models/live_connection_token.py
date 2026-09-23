from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LiveConnectionToken")


@_attrs_define
class LiveConnectionToken:
    """
    Attributes:
        token (str): Pass as the `token` field of the WebSocket `connect` command — see the "Live execution" guide.
        expires_at_ms (int):
    """

    token: str
    expires_at_ms: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        expires_at_ms = self.expires_at_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "token": token,
                "expiresAtMs": expires_at_ms,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        token = d.pop("token")

        expires_at_ms = d.pop("expiresAtMs")

        live_connection_token = cls(
            token=token,
            expires_at_ms=expires_at_ms,
        )

        live_connection_token.additional_properties = d
        return live_connection_token

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
