from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.signal_delivery_data import SignalDeliveryData
    from ..models.signal_notice_source import SignalNoticeSource


T = TypeVar("T", bound="SignalDelivery")


@_attrs_define
class SignalDelivery:
    """One notice due to one run a subscription feeds, and what its delivery did. Until `dueAtMs` it says that a notice is
    coming and when, not what it is about: `source` and `data` are present from `dueAtMs` on.

        Attributes:
            notice_id (str):
            received_at_ms (int):
            due_at_ms (int): When the notice was due to this subscription, its publication plus the subscription's `delay`.
            status (str): `PENDING`, `ATTACHED`, `REFUSED`, `EXPIRED` or `SKIPPED` (see `GET
                /signals/subscriptions/{subscriptionId}/deliveries`). The set may grow.
            run_id (str | Unset): The run the delivery is for.
            source (SignalNoticeSource | Unset): The instrument a notice is about: `LiveSourceRequest` without `type`, which
                is the subscription's to say, and with the instruments named one by one.
            data (SignalDeliveryData | Unset): The notice's text. Present from `dueAtMs` on.
            reason (str | Unset): Why it is `REFUSED` or `SKIPPED`. `REFUSED`: `PLAN_LIMIT` (a limit of your plan: the
                instruments a run may read, the pools you may follow at once, the runs you may have reading at once),
                `PLAN_REQUIRED` (your plan no longer includes live runs or subscriptions), `OTHER_FEED` (the run reads another
                market feed), `NOT_ACCEPTED` (the run's strategy does not accept that instrument or `type`) or `CAPACITY` (the
                platform had no room). `SKIPPED`: `NOT_RUNNING`, `UNSUBSCRIBED` (the run is no longer fed, or the subscription
                was cancelled), `ACCESS_REVOKED` (the provider revoked the code), `SUBSCRIPTION_EXPIRED` or `CHANNEL_DELETED`.
                The set may grow.
            message (str | Unset): A sentence saying more about a `REFUSED` delivery. Do not parse it.
            attachment_id (str | Unset): The attachment the delivery made, when it is `ATTACHED`.
            delivered_at_ms (int | Unset): When the delivery was made, or refused.
    """

    notice_id: str
    received_at_ms: int
    due_at_ms: int
    status: str
    run_id: str | Unset = UNSET
    source: SignalNoticeSource | Unset = UNSET
    data: SignalDeliveryData | Unset = UNSET
    reason: str | Unset = UNSET
    message: str | Unset = UNSET
    attachment_id: str | Unset = UNSET
    delivered_at_ms: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        notice_id = self.notice_id

        received_at_ms = self.received_at_ms

        due_at_ms = self.due_at_ms

        status = self.status

        run_id = self.run_id

        source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        reason = self.reason

        message = self.message

        attachment_id = self.attachment_id

        delivered_at_ms = self.delivered_at_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "noticeId": notice_id,
                "receivedAtMs": received_at_ms,
                "dueAtMs": due_at_ms,
                "status": status,
            }
        )
        if run_id is not UNSET:
            field_dict["runId"] = run_id
        if source is not UNSET:
            field_dict["source"] = source
        if data is not UNSET:
            field_dict["data"] = data
        if reason is not UNSET:
            field_dict["reason"] = reason
        if message is not UNSET:
            field_dict["message"] = message
        if attachment_id is not UNSET:
            field_dict["attachmentId"] = attachment_id
        if delivered_at_ms is not UNSET:
            field_dict["deliveredAtMs"] = delivered_at_ms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.signal_delivery_data import SignalDeliveryData
        from ..models.signal_notice_source import SignalNoticeSource

        d = dict(src_dict)
        notice_id = d.pop("noticeId")

        received_at_ms = d.pop("receivedAtMs")

        due_at_ms = d.pop("dueAtMs")

        status = d.pop("status")

        run_id = d.pop("runId", UNSET)

        _source = d.pop("source", UNSET)
        source: SignalNoticeSource | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = SignalNoticeSource.from_dict(_source)

        _data = d.pop("data", UNSET)
        data: SignalDeliveryData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = SignalDeliveryData.from_dict(_data)

        reason = d.pop("reason", UNSET)

        message = d.pop("message", UNSET)

        attachment_id = d.pop("attachmentId", UNSET)

        delivered_at_ms = d.pop("deliveredAtMs", UNSET)

        signal_delivery = cls(
            notice_id=notice_id,
            received_at_ms=received_at_ms,
            due_at_ms=due_at_ms,
            status=status,
            run_id=run_id,
            source=source,
            data=data,
            reason=reason,
            message=message,
            attachment_id=attachment_id,
            delivered_at_ms=delivered_at_ms,
        )

        signal_delivery.additional_properties = d
        return signal_delivery

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
