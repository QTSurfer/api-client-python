from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.insufficient_scope_error_code import InsufficientScopeErrorCode

T = TypeVar("T", bound="InsufficientScopeError")


@_attrs_define
class InsufficientScopeError:
    """Error envelope of a `403` returned when the API key behind the token does not carry the scope the operation needs.

    Attributes:
        code (InsufficientScopeErrorCode): Machine-readable error reason.
        message (str): Human-readable description of the failure.
        required (str): The scope the operation needs, as `resource:action`, in lower case. Example: datasets:write.
    """

    code: InsufficientScopeErrorCode
    message: str
    required: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code.value

        message = self.message

        required = self.required

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "message": message,
                "required": required,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = InsufficientScopeErrorCode(d.pop("code"))

        message = d.pop("message")

        required = d.pop("required")

        insufficient_scope_error = cls(
            code=code,
            message=message,
            required=required,
        )

        insufficient_scope_error.additional_properties = d
        return insufficient_scope_error

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
