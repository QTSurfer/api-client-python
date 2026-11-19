from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.auth_token_error_code import AuthTokenErrorCode
from ..models.auth_token_error_error import AuthTokenErrorError
from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthTokenError")


@_attrs_define
class AuthTokenError:
    """Error envelope returned by `POST /auth/token` (`403`) when the API key carries no scopes and scopes are required.

    Attributes:
        code (AuthTokenErrorCode): Machine-readable error reason.
        message (str): Human-readable description of the failure.
        error (AuthTokenErrorError | Unset): The same value as `code`; the field the other answers of this route carry.
    """

    code: AuthTokenErrorCode
    message: str
    error: AuthTokenErrorError | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code.value

        message = self.message

        error: str | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "message": message,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = AuthTokenErrorCode(d.pop("code"))

        message = d.pop("message")

        _error = d.pop("error", UNSET)
        error: AuthTokenErrorError | Unset
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = AuthTokenErrorError(_error)

        auth_token_error = cls(
            code=code,
            message=message,
            error=error,
        )

        auth_token_error.additional_properties = d
        return auth_token_error

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
