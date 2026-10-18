from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LiveSignalData")


@_attrs_define
class LiveSignalData:
    """The signal's own free-form payload, what the strategy put there with `signal.set(...)`. Whoever may read the run may
    read it, so on a `public` run it is public. A signal whose `data` is over 8 KiB (8,192 bytes of its JSON) is not
    pushed on the WebSocket channel, and `GET /live/{runId}/signals` returns it whole.

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        live_signal_data = cls()

        live_signal_data.additional_properties = d
        return live_signal_data

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
