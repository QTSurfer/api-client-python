from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.signal_subscription_run import SignalSubscriptionRun


T = TypeVar("T", bound="SignalSubscription")


@_attrs_define
class SignalSubscription:
    """What you bought by redeeming a code, and the runs it feeds now.

    Attributes:
        subscription_id (str):
        channel_id (str):
        delay (int): Seconds after a notice is published that it reaches your runs.
        max_runs (int): How many of your runs it feeds at once.
        state (str): `ACTIVE`, `EXPIRED` (past `expiresAtMs`: it feeds nothing until renewed), `REVOKED` (the provider
            revoked its code) or `ENDED` (you cancelled it, or the channel was deleted). The set may grow.
        runs (list[SignalSubscriptionRun]):
        created_at_ms (int):
        channel_name (str | Unset):
        expires_at_ms (int | Unset): When it expires. Absent when it does not.
        purchase_url (str | Unset): Where its offer is sold, to renew it.
    """

    subscription_id: str
    channel_id: str
    delay: int
    max_runs: int
    state: str
    runs: list[SignalSubscriptionRun]
    created_at_ms: int
    channel_name: str | Unset = UNSET
    expires_at_ms: int | Unset = UNSET
    purchase_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subscription_id = self.subscription_id

        channel_id = self.channel_id

        delay = self.delay

        max_runs = self.max_runs

        state = self.state

        runs = []
        for runs_item_data in self.runs:
            runs_item = runs_item_data.to_dict()
            runs.append(runs_item)

        created_at_ms = self.created_at_ms

        channel_name = self.channel_name

        expires_at_ms = self.expires_at_ms

        purchase_url = self.purchase_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subscriptionId": subscription_id,
                "channelId": channel_id,
                "delay": delay,
                "maxRuns": max_runs,
                "state": state,
                "runs": runs,
                "createdAtMs": created_at_ms,
            }
        )
        if channel_name is not UNSET:
            field_dict["channelName"] = channel_name
        if expires_at_ms is not UNSET:
            field_dict["expiresAtMs"] = expires_at_ms
        if purchase_url is not UNSET:
            field_dict["purchaseUrl"] = purchase_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.signal_subscription_run import SignalSubscriptionRun

        d = dict(src_dict)
        subscription_id = d.pop("subscriptionId")

        channel_id = d.pop("channelId")

        delay = d.pop("delay")

        max_runs = d.pop("maxRuns")

        state = d.pop("state")

        runs = []
        _runs = d.pop("runs")
        for runs_item_data in _runs:
            runs_item = SignalSubscriptionRun.from_dict(runs_item_data)

            runs.append(runs_item)

        created_at_ms = d.pop("createdAtMs")

        channel_name = d.pop("channelName", UNSET)

        expires_at_ms = d.pop("expiresAtMs", UNSET)

        purchase_url = d.pop("purchaseUrl", UNSET)

        signal_subscription = cls(
            subscription_id=subscription_id,
            channel_id=channel_id,
            delay=delay,
            max_runs=max_runs,
            state=state,
            runs=runs,
            created_at_ms=created_at_ms,
            channel_name=channel_name,
            expires_at_ms=expires_at_ms,
            purchase_url=purchase_url,
        )

        signal_subscription.additional_properties = d
        return signal_subscription

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
