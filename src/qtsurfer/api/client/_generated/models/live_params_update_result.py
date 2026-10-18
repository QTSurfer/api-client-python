from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LiveParamsUpdateResult")


@_attrs_define
class LiveParamsUpdateResult:
    """
    Attributes:
        run_id (str):
        params_version (int):
        effective_at_ms (int): Epoch milliseconds — the earliest moment the new values are guaranteed to be in effect.
    """

    run_id: str
    params_version: int
    effective_at_ms: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        run_id = self.run_id

        params_version = self.params_version

        effective_at_ms = self.effective_at_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "runId": run_id,
                "paramsVersion": params_version,
                "effectiveAtMs": effective_at_ms,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        run_id = d.pop("runId")

        params_version = d.pop("paramsVersion")

        effective_at_ms = d.pop("effectiveAtMs")

        live_params_update_result = cls(
            run_id=run_id,
            params_version=params_version,
            effective_at_ms=effective_at_ms,
        )

        live_params_update_result.additional_properties = d
        return live_params_update_result

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
