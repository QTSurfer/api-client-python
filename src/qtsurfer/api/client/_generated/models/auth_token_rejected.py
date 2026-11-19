from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.auth_token_rejected_error import AuthTokenRejectedError

T = TypeVar("T", bound="AuthTokenRejected")


@_attrs_define
class AuthTokenRejected:
    """Answer of `POST /auth/token` (`401`) when the API key is missing, unknown, revoked or expired.
    One value for all four: the route does not tell them apart.

        Attributes:
            error (AuthTokenRejectedError): Machine-readable reason.
    """

    error: AuthTokenRejectedError
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error = self.error.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "error": error,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error = AuthTokenRejectedError(d.pop("error"))

        auth_token_rejected = cls(
            error=error,
        )

        auth_token_rejected.additional_properties = d
        return auth_token_rejected

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
