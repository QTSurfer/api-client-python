from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.minted_signal_code import MintedSignalCode


T = TypeVar("T", bound="SignalMintedCodes")


@_attrs_define
class SignalMintedCodes:
    """The codes just minted, in clear. They are not shown again.

    Attributes:
        codes (list[MintedSignalCode]):
    """

    codes: list[MintedSignalCode]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        codes = []
        for codes_item_data in self.codes:
            codes_item = codes_item_data.to_dict()
            codes.append(codes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "codes": codes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.minted_signal_code import MintedSignalCode

        d = dict(src_dict)
        codes = []
        _codes = d.pop("codes")
        for codes_item_data in _codes:
            codes_item = MintedSignalCode.from_dict(codes_item_data)

            codes.append(codes_item)

        signal_minted_codes = cls(
            codes=codes,
        )

        signal_minted_codes.additional_properties = d
        return signal_minted_codes

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
