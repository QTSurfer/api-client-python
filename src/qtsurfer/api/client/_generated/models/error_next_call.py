from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.error_next_call_method import ErrorNextCallMethod
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_next_call_body import ErrorNextCallBody


T = TypeVar("T", bound="ErrorNextCall")


@_attrs_define
class ErrorNextCall:
    """The call that gets past an error, ready to send: a client that wants the same thing by
    another route makes this request. Present only on an error that has one.

        Attributes:
            method (ErrorNextCallMethod): HTTP method of the call. Example: POST.
            path (str): Path of the call, relative to the server URL (the one that already ends in `/v1`). Example:
                /datasets/imports.
            body (ErrorNextCallBody | Unset): JSON body of the call, when it has one. Whatever depends on the caller and
                cannot be
                known here (such as the `name` of a dataset) is left for the client to add.
    """

    method: ErrorNextCallMethod
    path: str
    body: ErrorNextCallBody | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method = self.method.value

        path = self.path

        body: dict[str, Any] | Unset = UNSET
        if not isinstance(self.body, Unset):
            body = self.body.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "method": method,
                "path": path,
            }
        )
        if body is not UNSET:
            field_dict["body"] = body

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_next_call_body import ErrorNextCallBody

        d = dict(src_dict)
        method = ErrorNextCallMethod(d.pop("method"))

        path = d.pop("path")

        _body = d.pop("body", UNSET)
        body: ErrorNextCallBody | Unset
        if isinstance(_body, Unset):
            body = UNSET
        else:
            body = ErrorNextCallBody.from_dict(_body)

        error_next_call = cls(
            method=method,
            path=path,
            body=body,
        )

        error_next_call.additional_properties = d
        return error_next_call

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
