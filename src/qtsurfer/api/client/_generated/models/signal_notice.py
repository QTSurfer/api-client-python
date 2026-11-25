from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.signal_delivery_counts import SignalDeliveryCounts
    from ..models.signal_notice_data import SignalNoticeData
    from ..models.signal_notice_source import SignalNoticeSource


T = TypeVar("T", bound="SignalNotice")


@_attrs_define
class SignalNotice:
    """
    Attributes:
        notice_id (str):
        source (SignalNoticeSource): The instrument a notice is about: `LiveSourceRequest` without `type`, which is the
            subscription's to say, and with the instruments named one by one.
        received_at_ms (int):
        expires_at_ms (int):
        deliveries (SignalDeliveryCounts): How the deliveries of a notice stand, by status (see `SignalDelivery`).
        ref (str | Unset):
        data (SignalNoticeData | Unset):
    """

    notice_id: str
    source: SignalNoticeSource
    received_at_ms: int
    expires_at_ms: int
    deliveries: SignalDeliveryCounts
    ref: str | Unset = UNSET
    data: SignalNoticeData | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        notice_id = self.notice_id

        source = self.source.to_dict()

        received_at_ms = self.received_at_ms

        expires_at_ms = self.expires_at_ms

        deliveries = self.deliveries.to_dict()

        ref = self.ref

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "noticeId": notice_id,
                "source": source,
                "receivedAtMs": received_at_ms,
                "expiresAtMs": expires_at_ms,
                "deliveries": deliveries,
            }
        )
        if ref is not UNSET:
            field_dict["ref"] = ref
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.signal_delivery_counts import SignalDeliveryCounts
        from ..models.signal_notice_data import SignalNoticeData
        from ..models.signal_notice_source import SignalNoticeSource

        d = dict(src_dict)
        notice_id = d.pop("noticeId")

        source = SignalNoticeSource.from_dict(d.pop("source"))

        received_at_ms = d.pop("receivedAtMs")

        expires_at_ms = d.pop("expiresAtMs")

        deliveries = SignalDeliveryCounts.from_dict(d.pop("deliveries"))

        ref = d.pop("ref", UNSET)

        _data = d.pop("data", UNSET)
        data: SignalNoticeData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = SignalNoticeData.from_dict(_data)

        signal_notice = cls(
            notice_id=notice_id,
            source=source,
            received_at_ms=received_at_ms,
            expires_at_ms=expires_at_ms,
            deliveries=deliveries,
            ref=ref,
            data=data,
        )

        signal_notice.additional_properties = d
        return signal_notice

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
