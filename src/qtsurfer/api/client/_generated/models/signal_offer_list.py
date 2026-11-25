from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.signal_offer import SignalOffer


T = TypeVar("T", bound="SignalOfferList")


@_attrs_define
class SignalOfferList:
    """
    Attributes:
        offers (list[SignalOffer]):
    """

    offers: list[SignalOffer]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        offers = []
        for offers_item_data in self.offers:
            offers_item = offers_item_data.to_dict()
            offers.append(offers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "offers": offers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.signal_offer import SignalOffer

        d = dict(src_dict)
        offers = []
        _offers = d.pop("offers")
        for offers_item_data in _offers:
            offers_item = SignalOffer.from_dict(offers_item_data)

            offers.append(offers_item)

        signal_offer_list = cls(
            offers=offers,
        )

        signal_offer_list.additional_properties = d
        return signal_offer_list

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
