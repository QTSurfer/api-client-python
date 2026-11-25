from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MintedSignalCode")


@_attrs_define
class MintedSignalCode:
    """
    Attributes:
        code_id (str):
        code (str): The code to hand to the buyer. Keep it secret until then.
        prefix (str): Its first characters, as `GET /signals/offers/{offerId}/codes` shows it.
    """

    code_id: str
    code: str
    prefix: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code_id = self.code_id

        code = self.code

        prefix = self.prefix

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "codeId": code_id,
                "code": code,
                "prefix": prefix,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code_id = d.pop("codeId")

        code = d.pop("code")

        prefix = d.pop("prefix")

        minted_signal_code = cls(
            code_id=code_id,
            code=code,
            prefix=prefix,
        )

        minted_signal_code.additional_properties = d
        return minted_signal_code

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
