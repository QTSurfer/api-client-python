from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.live_source import LiveSource


T = TypeVar("T", bound="LiveAttachment")


@_attrs_define
class LiveAttachment:
    """One market-data source attached to a live run.

    Attributes:
        attachment_id (str):
        source (LiveSource): One market-data source a live run reads. A run starts with one, or none, and more can be
            attached afterwards on the same market feed (see `attachments`).
        state (str): `ATTACHING` (accepted; it takes effect at `effectiveAtMs`), `ATTACHED` (the run is reading it),
            `DETACHING` (a detach is accepted), `DETACHED` (the run no longer reads it) or `REFUSED` (the platform could not
            follow it; the run stays as it was). The set may grow: read an unknown value as a source in transition.
        created_at_ms (int):
        warm_from (int | Unset): The seconds of warm-up in effect for this source.
        resolve_instrument (bool | Unset): The value in effect for this source: how the strategy is told of a `dex`
            pool. See "The instrument of a pool" in the Live execution guide.
        ref (str | Unset): The `ref` it was attached with, when there was one.
        reason (str | Unset): Why it is `DETACHED` or `REFUSED`, when there is something to say: `OWNER` (you detached
            it), `REFUSED` (the platform refused it), `POOL_GONE` (a `dex` pool stopped being followed), `CAPACITY` (the
            platform has no room to follow it), `STRATEGY` (the strategy asked for it) or `NO_DATA` (an instrument of a
            centralized exchange that the platform does not capture sent nothing for five minutes). The set may grow.
        message (str | Unset): A sentence saying more about a `REFUSED` attachment. Do not parse it.
        effective_at_ms (int | Unset): Epoch milliseconds, when the last change to this attachment takes effect.
    """

    attachment_id: str
    source: LiveSource
    state: str
    created_at_ms: int
    warm_from: int | Unset = UNSET
    resolve_instrument: bool | Unset = UNSET
    ref: str | Unset = UNSET
    reason: str | Unset = UNSET
    message: str | Unset = UNSET
    effective_at_ms: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attachment_id = self.attachment_id

        source = self.source.to_dict()

        state = self.state

        created_at_ms = self.created_at_ms

        warm_from = self.warm_from

        resolve_instrument = self.resolve_instrument

        ref = self.ref

        reason = self.reason

        message = self.message

        effective_at_ms = self.effective_at_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attachmentId": attachment_id,
                "source": source,
                "state": state,
                "createdAtMs": created_at_ms,
            }
        )
        if warm_from is not UNSET:
            field_dict["warmFrom"] = warm_from
        if resolve_instrument is not UNSET:
            field_dict["resolveInstrument"] = resolve_instrument
        if ref is not UNSET:
            field_dict["ref"] = ref
        if reason is not UNSET:
            field_dict["reason"] = reason
        if message is not UNSET:
            field_dict["message"] = message
        if effective_at_ms is not UNSET:
            field_dict["effectiveAtMs"] = effective_at_ms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.live_source import LiveSource

        d = dict(src_dict)
        attachment_id = d.pop("attachmentId")

        source = LiveSource.from_dict(d.pop("source"))

        state = d.pop("state")

        created_at_ms = d.pop("createdAtMs")

        warm_from = d.pop("warmFrom", UNSET)

        resolve_instrument = d.pop("resolveInstrument", UNSET)

        ref = d.pop("ref", UNSET)

        reason = d.pop("reason", UNSET)

        message = d.pop("message", UNSET)

        effective_at_ms = d.pop("effectiveAtMs", UNSET)

        live_attachment = cls(
            attachment_id=attachment_id,
            source=source,
            state=state,
            created_at_ms=created_at_ms,
            warm_from=warm_from,
            resolve_instrument=resolve_instrument,
            ref=ref,
            reason=reason,
            message=message,
            effective_at_ms=effective_at_ms,
        )

        live_attachment.additional_properties = d
        return live_attachment

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
