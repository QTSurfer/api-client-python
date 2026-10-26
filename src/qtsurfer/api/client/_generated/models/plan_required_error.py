from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_next_call import ErrorNextCall


T = TypeVar("T", bound="PlanRequiredError")


@_attrs_define
class PlanRequiredError:
    """The error of a `402`: your plan does not include what the request asks for. It is a
    `ResponseError` (`retryable` is `false`) plus `upgradeUrl`.

        Attributes:
            code (int): Status code Example: 400.
            message (str): Error description Example: Invalid request.
            reason (str | Unset): A stable token naming the cause, for a client to branch on without reading `message`.
                Present only on an error that has one, and each operation that can return one lists
                the values it uses. A client treats a value it does not know like an absent `reason`.
                 Example: OUTSIDE_WINDOW.
            retryable (bool | Unset): Whether sending the same request again can succeed. `true` for `408`, `425`, `429` and
                every `5xx`; `false` for every other `4xx`, which fails the same way until the request
                changes: a field of the wrong type, a strategy that does not compile, a missing
                parameter. A plan limit (a `402`, or a `429` without `Retry-After`) is `false`. When the answer
                carries a `Retry-After`, wait that long before sending the request again.
            next_ (ErrorNextCall | Unset): The call that gets past an error, ready to send: a client that wants the same
                thing by
                another route makes this request. Present only on an error that has one.
            upgrade_url (str | Unset): The page where the plan can be changed. Present only when the platform has one for
                this
                environment; absent otherwise. A `402` is the only error that carries it.
                 Example: https://example.com/upgrade.
    """

    code: int
    message: str
    reason: str | Unset = UNSET
    retryable: bool | Unset = UNSET
    next_: ErrorNextCall | Unset = UNSET
    upgrade_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        reason = self.reason

        retryable = self.retryable

        next_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.next_, Unset):
            next_ = self.next_.to_dict()

        upgrade_url = self.upgrade_url

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
        if retryable is not UNSET:
            field_dict["retryable"] = retryable
        if next_ is not UNSET:
            field_dict["next"] = next_
        if upgrade_url is not UNSET:
            field_dict["upgradeUrl"] = upgrade_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_next_call import ErrorNextCall

        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message")

        reason = d.pop("reason", UNSET)

        retryable = d.pop("retryable", UNSET)

        _next_ = d.pop("next", UNSET)
        next_: ErrorNextCall | Unset
        if isinstance(_next_, Unset):
            next_ = UNSET
        else:
            next_ = ErrorNextCall.from_dict(_next_)

        upgrade_url = d.pop("upgradeUrl", UNSET)

        plan_required_error = cls(
            code=code,
            message=message,
            reason=reason,
            retryable=retryable,
            next_=next_,
            upgrade_url=upgrade_url,
        )

        plan_required_error.additional_properties = d
        return plan_required_error

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
