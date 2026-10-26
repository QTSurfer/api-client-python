from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PrepareAccepted")


@_attrs_define
class PrepareAccepted:
    """The `202` of a prepare: the job and the cadence the data is prepared at.

    Example:
        {'jobId': '13RBLGQlPnfDjO6wyKSX8i', 'cadence': '3m'}

    Attributes:
        job_id (str): Unique job identifier; use this to poll for completion. For a sweep, pass this same value as the
            `requestId` path parameter to `executeSweep` — same identifier, different name at that call site. Example:
            13RBLGQlPnfDjO6wyKSX8i.
        cadence (str): The cadence in effect: the one you asked for, or the plan's default when you asked for
            none. For `exchangeId: user`, the dataset's own cadence when you asked for none.
             Example: 3m.
    """

    job_id: str
    cadence: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_id = self.job_id

        cadence = self.cadence

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "jobId": job_id,
                "cadence": cadence,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        job_id = d.pop("jobId")

        cadence = d.pop("cadence")

        prepare_accepted = cls(
            job_id=job_id,
            cadence=cadence,
        )

        prepare_accepted.additional_properties = d
        return prepare_accepted

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
