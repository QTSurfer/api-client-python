from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dataset_version_timestamp_unit import DatasetVersionTimestampUnit
from ..types import UNSET, Unset

T = TypeVar("T", bound="DatasetVersion")


@_attrs_define
class DatasetVersion:
    """One successfully ingested upload. Cadence and timestamp unit are discovered from the file,
    not declared by the caller.

        Attributes:
            dataset_id (str):  Example: ds_3f9a1c2e7b0d4a5f.
            id (str | Unset): The version id. Pass as `datasetVersionId` on `POST .../prepare` to pin it. Example:
                dsv_8e2b4f19c6a03d7e.
            bytes_ (int | Unset): Size of the uploaded file. Example: 4831022.
            rows (int | Unset): Number of data rows. Example: 86400.
            cadence (str | Unset): The discovered bar cadence (e.g. `1s`, `1m`, `1h`). Example: 1s.
            timestamp_unit (DatasetVersionTimestampUnit | Unset): The unit the `timestamp` column was uploaded in —
                ISO-8601, or the epoch band its
                numeric values fell in (seconds, millis, or micros).
                 Example: iso.
            gaps (int | Unset): Number of gaps at the discovered cadence.
            largest_gap_steps (int | Unset): The largest gap, in units of the discovered cadence step.
    """

    dataset_id: str
    id: str | Unset = UNSET
    bytes_: int | Unset = UNSET
    rows: int | Unset = UNSET
    cadence: str | Unset = UNSET
    timestamp_unit: DatasetVersionTimestampUnit | Unset = UNSET
    gaps: int | Unset = UNSET
    largest_gap_steps: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dataset_id = self.dataset_id

        id = self.id

        bytes_ = self.bytes_

        rows = self.rows

        cadence = self.cadence

        timestamp_unit: str | Unset = UNSET
        if not isinstance(self.timestamp_unit, Unset):
            timestamp_unit = self.timestamp_unit.value

        gaps = self.gaps

        largest_gap_steps = self.largest_gap_steps

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "datasetId": dataset_id,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if bytes_ is not UNSET:
            field_dict["bytes"] = bytes_
        if rows is not UNSET:
            field_dict["rows"] = rows
        if cadence is not UNSET:
            field_dict["cadence"] = cadence
        if timestamp_unit is not UNSET:
            field_dict["timestampUnit"] = timestamp_unit
        if gaps is not UNSET:
            field_dict["gaps"] = gaps
        if largest_gap_steps is not UNSET:
            field_dict["largestGapSteps"] = largest_gap_steps

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dataset_id = d.pop("datasetId")

        id = d.pop("id", UNSET)

        bytes_ = d.pop("bytes", UNSET)

        rows = d.pop("rows", UNSET)

        cadence = d.pop("cadence", UNSET)

        _timestamp_unit = d.pop("timestampUnit", UNSET)
        timestamp_unit: DatasetVersionTimestampUnit | Unset
        if isinstance(_timestamp_unit, Unset):
            timestamp_unit = UNSET
        else:
            timestamp_unit = DatasetVersionTimestampUnit(_timestamp_unit)

        gaps = d.pop("gaps", UNSET)

        largest_gap_steps = d.pop("largestGapSteps", UNSET)

        dataset_version = cls(
            dataset_id=dataset_id,
            id=id,
            bytes_=bytes_,
            rows=rows,
            cadence=cadence,
            timestamp_unit=timestamp_unit,
            gaps=gaps,
            largest_gap_steps=largest_gap_steps,
        )

        dataset_version.additional_properties = d
        return dataset_version

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
