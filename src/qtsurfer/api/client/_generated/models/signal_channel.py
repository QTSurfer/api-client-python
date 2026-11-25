from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.signal_channel_visibility import SignalChannelVisibility
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.signal_offer import SignalOffer


T = TypeVar("T", bound="SignalChannel")


@_attrs_define
class SignalChannel:
    """A signal channel. `webhookUrl` and `subscriptions` are present only for its owner, and so are the ids and counts of
    its `offers`.

        Attributes:
            channel_id (str):
            name (str):
            visibility (SignalChannelVisibility):
            delays (list[int]): The delays of its offers, in seconds, smallest first, each once.
            created_at_ms (int):
            description (str | Unset):
            offers (list[SignalOffer] | Unset): What the channel sells, oldest first.
            webhook_url (str | Unset): Owner only. The secret address that publishes a notice without a token (`POST
                /signals/hook/{hookKey}`).
            subscriptions (int | Unset): Owner only. How many subscriptions are active and not expired. Who holds them is
                never shown.
    """

    channel_id: str
    name: str
    visibility: SignalChannelVisibility
    delays: list[int]
    created_at_ms: int
    description: str | Unset = UNSET
    offers: list[SignalOffer] | Unset = UNSET
    webhook_url: str | Unset = UNSET
    subscriptions: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel_id = self.channel_id

        name = self.name

        visibility = self.visibility.value

        delays = self.delays

        created_at_ms = self.created_at_ms

        description = self.description

        offers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.offers, Unset):
            offers = []
            for offers_item_data in self.offers:
                offers_item = offers_item_data.to_dict()
                offers.append(offers_item)

        webhook_url = self.webhook_url

        subscriptions = self.subscriptions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "channelId": channel_id,
                "name": name,
                "visibility": visibility,
                "delays": delays,
                "createdAtMs": created_at_ms,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if offers is not UNSET:
            field_dict["offers"] = offers
        if webhook_url is not UNSET:
            field_dict["webhookUrl"] = webhook_url
        if subscriptions is not UNSET:
            field_dict["subscriptions"] = subscriptions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.signal_offer import SignalOffer

        d = dict(src_dict)
        channel_id = d.pop("channelId")

        name = d.pop("name")

        visibility = SignalChannelVisibility(d.pop("visibility"))

        delays = cast(list[int], d.pop("delays"))

        created_at_ms = d.pop("createdAtMs")

        description = d.pop("description", UNSET)

        _offers = d.pop("offers", UNSET)
        offers: list[SignalOffer] | Unset = UNSET
        if _offers is not UNSET:
            offers = []
            for offers_item_data in _offers:
                offers_item = SignalOffer.from_dict(offers_item_data)

                offers.append(offers_item)

        webhook_url = d.pop("webhookUrl", UNSET)

        subscriptions = d.pop("subscriptions", UNSET)

        signal_channel = cls(
            channel_id=channel_id,
            name=name,
            visibility=visibility,
            delays=delays,
            created_at_ms=created_at_ms,
            description=description,
            offers=offers,
            webhook_url=webhook_url,
            subscriptions=subscriptions,
        )

        signal_channel.additional_properties = d
        return signal_channel

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
