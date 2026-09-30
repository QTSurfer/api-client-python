from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LiveCommandResult")


@_attrs_define
class LiveCommandResult:
    """
    Attributes:
        run_id (str):
        command_id (str): This command's own id, generated fresh for this call. A retried request is a second, distinct
            command — this endpoint takes no idempotency key.
        effective_at_ms (int): Epoch milliseconds — the market position every execution applies this command at.
    """

    run_id: str
    command_id: str
    effective_at_ms: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        run_id = self.run_id

        command_id = self.command_id

        effective_at_ms = self.effective_at_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "runId": run_id,
                "commandId": command_id,
                "effectiveAtMs": effective_at_ms,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        run_id = d.pop("runId")

        command_id = d.pop("commandId")

        effective_at_ms = d.pop("effectiveAtMs")

        live_command_result = cls(
            run_id=run_id,
            command_id=command_id,
            effective_at_ms=effective_at_ms,
        )

        live_command_result.additional_properties = d
        return live_command_result

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
