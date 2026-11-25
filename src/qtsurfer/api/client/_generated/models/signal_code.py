from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SignalCode")


@_attrs_define
class SignalCode:
    """
    Attributes:
        code_id (str):
        prefix (str):
        state (str): `UNUSED`, `REDEEMED` or `REVOKED`. Who redeemed it is never shown.
        created_at_ms (int):
        redeemed_at_ms (int | Unset):
    """

    code_id: str
    prefix: str
    state: str
    created_at_ms: int
    redeemed_at_ms: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code_id = self.code_id

        prefix = self.prefix

        state = self.state

        created_at_ms = self.created_at_ms

        redeemed_at_ms = self.redeemed_at_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "codeId": code_id,
                "prefix": prefix,
                "state": state,
                "createdAtMs": created_at_ms,
            }
        )
        if redeemed_at_ms is not UNSET:
            field_dict["redeemedAtMs"] = redeemed_at_ms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code_id = d.pop("codeId")

        prefix = d.pop("prefix")

        state = d.pop("state")

        created_at_ms = d.pop("createdAtMs")

        redeemed_at_ms = d.pop("redeemedAtMs", UNSET)

        signal_code = cls(
            code_id=code_id,
            prefix=prefix,
            state=state,
            created_at_ms=created_at_ms,
            redeemed_at_ms=redeemed_at_ms,
        )

        signal_code.additional_properties = d
        return signal_code

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
