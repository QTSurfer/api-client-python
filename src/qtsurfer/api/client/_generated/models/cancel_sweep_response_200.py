from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cancel_sweep_response_200_status import CancelSweepResponse200Status

T = TypeVar("T", bound="CancelSweepResponse200")


@_attrs_define
class CancelSweepResponse200:
    """
    Attributes:
        status (CancelSweepResponse200Status):
        sweep_id (str):
    """

    status: CancelSweepResponse200Status
    sweep_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        sweep_id = self.sweep_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "sweepId": sweep_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = CancelSweepResponse200Status(d.pop("status"))

        sweep_id = d.pop("sweepId")

        cancel_sweep_response_200 = cls(
            status=status,
            sweep_id=sweep_id,
        )

        cancel_sweep_response_200.additional_properties = d
        return cancel_sweep_response_200

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
