from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hal_link import HalLink


T = TypeVar("T", bound="InstrumentLinks")


@_attrs_define
class InstrumentLinks:
    """HAL `_links` — segment discovery for the instruments listing

    Attributes:
        self_ (HalLink): A HAL link object (Hypertext Application Language)
        spot (HalLink | Unset): A HAL link object (Hypertext Application Language)
        futures (HalLink | Unset): A HAL link object (Hypertext Application Language)
    """

    self_: HalLink
    spot: HalLink | Unset = UNSET
    futures: HalLink | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_ = self.self_.to_dict()

        spot: dict[str, Any] | Unset = UNSET
        if not isinstance(self.spot, Unset):
            spot = self.spot.to_dict()

        futures: dict[str, Any] | Unset = UNSET
        if not isinstance(self.futures, Unset):
            futures = self.futures.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "self": self_,
            }
        )
        if spot is not UNSET:
            field_dict["spot"] = spot
        if futures is not UNSET:
            field_dict["futures"] = futures

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hal_link import HalLink

        d = dict(src_dict)
        self_ = HalLink.from_dict(d.pop("self"))

        _spot = d.pop("spot", UNSET)
        spot: HalLink | Unset
        if isinstance(_spot, Unset):
            spot = UNSET
        else:
            spot = HalLink.from_dict(_spot)

        _futures = d.pop("futures", UNSET)
        futures: HalLink | Unset
        if isinstance(_futures, Unset):
            futures = UNSET
        else:
            futures = HalLink.from_dict(_futures)

        instrument_links = cls(
            self_=self_,
            spot=spot,
            futures=futures,
        )

        instrument_links.additional_properties = d
        return instrument_links

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
