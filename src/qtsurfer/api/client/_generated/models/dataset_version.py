from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dataset_version_data_format import DatasetVersionDataFormat
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
            bytes_ (int | Unset): Size of the stored file `dataUrl` points at — a converted `lastra` for a CSV/gzip/zip
                upload, or the parquet file itself, unconverted, for a parquet upload. Not the size of the bytes originally PUT
                to storage; see `dataFormat`. Example: 4831022.
            rows (int | Unset): Number of data rows. Example: 86400.
            cadence (str | Unset): The discovered bar cadence (e.g. `1s`, `1m`, `1h`). Example: 1s.
            timestamp_unit (DatasetVersionTimestampUnit | Unset): The unit the `timestamp` column was uploaded in —
                ISO-8601, or the epoch band its
                numeric values fell in (seconds, millis, or micros).
                 Example: iso.
            gaps (int | Unset): Number of gaps at the discovered cadence.
            largest_gap_steps (int | Unset): The largest gap, in units of the discovered cadence step.
            data_url (str | Unset): Presigned GET URL to the stored file — see `dataFormat` for which format it's in.
                Present once the version is `ready`. Long-lived (day-scale, not permanent): a
                DuckDB-WASM/`lastra-ts`-style reader issues HTTP range requests against it lazily over
                an extended viewing session, not in one shot like a browser upload.
                 Example: https://storage.qtsurfer.com/00000000-
                .../ds_3f9a1c2e7b0d4a5f/dsv_8e2b4f19c6a03d7e/ticker_BTC_USDT_1700000000000_1700086400000_1m.lastra?X-Amz-....
            data_format (DatasetVersionDataFormat | Unset): Which format `dataUrl` is actually in — check this rather than
                assuming it matches
                how you uploaded it. `lastra` — our native columnar format — for a CSV (or gzip/zip
                of one) upload, always converted on ingest. `parquet` for a parquet upload, stored
                as-is today.
                 Example: lastra.
    """

    dataset_id: str
    id: str | Unset = UNSET
    bytes_: int | Unset = UNSET
    rows: int | Unset = UNSET
    cadence: str | Unset = UNSET
    timestamp_unit: DatasetVersionTimestampUnit | Unset = UNSET
    gaps: int | Unset = UNSET
    largest_gap_steps: int | Unset = UNSET
    data_url: str | Unset = UNSET
    data_format: DatasetVersionDataFormat | Unset = UNSET
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

        data_url = self.data_url

        data_format: str | Unset = UNSET
        if not isinstance(self.data_format, Unset):
            data_format = self.data_format.value

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
        if data_url is not UNSET:
            field_dict["dataUrl"] = data_url
        if data_format is not UNSET:
            field_dict["dataFormat"] = data_format

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

        data_url = d.pop("dataUrl", UNSET)

        _data_format = d.pop("dataFormat", UNSET)
        data_format: DatasetVersionDataFormat | Unset
        if isinstance(_data_format, Unset):
            data_format = UNSET
        else:
            data_format = DatasetVersionDataFormat(_data_format)

        dataset_version = cls(
            dataset_id=dataset_id,
            id=id,
            bytes_=bytes_,
            rows=rows,
            cadence=cadence,
            timestamp_unit=timestamp_unit,
            gaps=gaps,
            largest_gap_steps=largest_gap_steps,
            data_url=data_url,
            data_format=data_format,
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
