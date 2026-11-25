from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.signal_offer_codes import SignalOfferCodes


T = TypeVar("T", bound="SignalOffer")


@_attrs_define
class SignalOffer:
    """What a channel sells. `offerId`, `createdAtMs`, `codes`, `subscriptions` and `runs` are present only for the
    channel's owner.

        Attributes:
            delay (int):
            max_runs (int):
            offer_id (str | Unset):
            duration_days (int | Unset): Absent when a subscription of this offer does not expire.
            purchase_url (str | Unset):
            created_at_ms (int | Unset):
            codes (SignalOfferCodes | Unset):
            subscriptions (int | Unset): Subscriptions of this offer active and not expired now.
            runs (int | Unset): Runs those subscriptions feed now.
    """

    delay: int
    max_runs: int
    offer_id: str | Unset = UNSET
    duration_days: int | Unset = UNSET
    purchase_url: str | Unset = UNSET
    created_at_ms: int | Unset = UNSET
    codes: SignalOfferCodes | Unset = UNSET
    subscriptions: int | Unset = UNSET
    runs: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delay = self.delay

        max_runs = self.max_runs

        offer_id = self.offer_id

        duration_days = self.duration_days

        purchase_url = self.purchase_url

        created_at_ms = self.created_at_ms

        codes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.codes, Unset):
            codes = self.codes.to_dict()

        subscriptions = self.subscriptions

        runs = self.runs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "delay": delay,
                "maxRuns": max_runs,
            }
        )
        if offer_id is not UNSET:
            field_dict["offerId"] = offer_id
        if duration_days is not UNSET:
            field_dict["durationDays"] = duration_days
        if purchase_url is not UNSET:
            field_dict["purchaseUrl"] = purchase_url
        if created_at_ms is not UNSET:
            field_dict["createdAtMs"] = created_at_ms
        if codes is not UNSET:
            field_dict["codes"] = codes
        if subscriptions is not UNSET:
            field_dict["subscriptions"] = subscriptions
        if runs is not UNSET:
            field_dict["runs"] = runs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.signal_offer_codes import SignalOfferCodes

        d = dict(src_dict)
        delay = d.pop("delay")

        max_runs = d.pop("maxRuns")

        offer_id = d.pop("offerId", UNSET)

        duration_days = d.pop("durationDays", UNSET)

        purchase_url = d.pop("purchaseUrl", UNSET)

        created_at_ms = d.pop("createdAtMs", UNSET)

        _codes = d.pop("codes", UNSET)
        codes: SignalOfferCodes | Unset
        if isinstance(_codes, Unset):
            codes = UNSET
        else:
            codes = SignalOfferCodes.from_dict(_codes)

        subscriptions = d.pop("subscriptions", UNSET)

        runs = d.pop("runs", UNSET)

        signal_offer = cls(
            delay=delay,
            max_runs=max_runs,
            offer_id=offer_id,
            duration_days=duration_days,
            purchase_url=purchase_url,
            created_at_ms=created_at_ms,
            codes=codes,
            subscriptions=subscriptions,
            runs=runs,
        )

        signal_offer.additional_properties = d
        return signal_offer

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
