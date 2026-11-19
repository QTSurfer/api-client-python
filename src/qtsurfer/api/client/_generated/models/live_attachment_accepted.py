from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.live_attachment_accepted_state import LiveAttachmentAcceptedState
from ..types import UNSET, Unset

T = TypeVar("T", bound="LiveAttachmentAccepted")


@_attrs_define
class LiveAttachmentAccepted:
    """
    Attributes:
        attachment_id (str):
        state (LiveAttachmentAcceptedState): The attachment's state when the request was answered. See `LiveAttachment`.
        effective_at_ms (int | Unset): Epoch milliseconds, the moment every execution behind the run applies the change
            at the same market position. Absent when the run was waiting and the change is its start.
    """

    attachment_id: str
    state: LiveAttachmentAcceptedState
    effective_at_ms: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attachment_id = self.attachment_id

        state = self.state.value

        effective_at_ms = self.effective_at_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attachmentId": attachment_id,
                "state": state,
            }
        )
        if effective_at_ms is not UNSET:
            field_dict["effectiveAtMs"] = effective_at_ms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attachment_id = d.pop("attachmentId")

        state = LiveAttachmentAcceptedState(d.pop("state"))

        effective_at_ms = d.pop("effectiveAtMs", UNSET)

        live_attachment_accepted = cls(
            attachment_id=attachment_id,
            state=state,
            effective_at_ms=effective_at_ms,
        )

        live_attachment_accepted.additional_properties = d
        return live_attachment_accepted

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
