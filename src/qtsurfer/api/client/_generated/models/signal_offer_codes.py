from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SignalOfferCodes")


@_attrs_define
class SignalOfferCodes:
    """
    Attributes:
        minted (int | Unset):
        redeemed (int | Unset):
    """

    minted: int | Unset = UNSET
    redeemed: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        minted = self.minted

        redeemed = self.redeemed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if minted is not UNSET:
            field_dict["minted"] = minted
        if redeemed is not UNSET:
            field_dict["redeemed"] = redeemed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        minted = d.pop("minted", UNSET)

        redeemed = d.pop("redeemed", UNSET)

        signal_offer_codes = cls(
            minted=minted,
            redeemed=redeemed,
        )

        signal_offer_codes.additional_properties = d
        return signal_offer_codes

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
