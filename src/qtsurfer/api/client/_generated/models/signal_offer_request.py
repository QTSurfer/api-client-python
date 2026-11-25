from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SignalOfferRequest")


@_attrs_define
class SignalOfferRequest:
    """
    Attributes:
        delay (int): Seconds after a notice is published that it reaches the runs of a subscription of this offer.
        max_runs (int): How many of the buyer's runs one subscription feeds at once.
        duration_days (int | Unset): How long a subscription lasts from the moment its code is redeemed, and what a
            renewal adds. Left out, it does not expire.
        purchase_url (str | Unset): Where you sell it, shown with the channel. `https` only.
    """

    delay: int
    max_runs: int
    duration_days: int | Unset = UNSET
    purchase_url: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        delay = self.delay

        max_runs = self.max_runs

        duration_days = self.duration_days

        purchase_url = self.purchase_url

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "delay": delay,
                "maxRuns": max_runs,
            }
        )
        if duration_days is not UNSET:
            field_dict["durationDays"] = duration_days
        if purchase_url is not UNSET:
            field_dict["purchaseUrl"] = purchase_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        delay = d.pop("delay")

        max_runs = d.pop("maxRuns")

        duration_days = d.pop("durationDays", UNSET)

        purchase_url = d.pop("purchaseUrl", UNSET)

        signal_offer_request = cls(
            delay=delay,
            max_runs=max_runs,
            duration_days=duration_days,
            purchase_url=purchase_url,
        )

        return signal_offer_request
