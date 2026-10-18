from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_next_call import ErrorNextCall


T = TypeVar("T", bound="ResponseError")


@_attrs_define
class ResponseError:
    """General response error

    Attributes:
        code (int): Status code Example: 400.
        message (str): Error description Example: Invalid request.
        reason (str | Unset): A stable token naming the cause, for a client to branch on without reading `message`.
            Present only on an error that has one, and each operation that can return one lists
            the values it uses. A client treats a value it does not know like an absent `reason`.
             Example: OUTSIDE_WINDOW.
        next_ (ErrorNextCall | Unset): The call that gets past an error, ready to send: a client that wants the same
            thing by
            another route makes this request. Present only on an error that has one.
    """

    code: int
    message: str
    reason: str | Unset = UNSET
    next_: ErrorNextCall | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        reason = self.reason

        next_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.next_, Unset):
            next_ = self.next_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "message": message,
            }
        )
        if reason is not UNSET:
            field_dict["reason"] = reason
        if next_ is not UNSET:
            field_dict["next"] = next_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_next_call import ErrorNextCall

        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message")

        reason = d.pop("reason", UNSET)

        _next_ = d.pop("next", UNSET)
        next_: ErrorNextCall | Unset
        if isinstance(_next_, Unset):
            next_ = UNSET
        else:
            next_ = ErrorNextCall.from_dict(_next_)

        response_error = cls(
            code=code,
            message=message,
            reason=reason,
            next_=next_,
        )

        response_error.additional_properties = d
        return response_error

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
