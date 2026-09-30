from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.dataset_status import DatasetStatus
from ..models.dataset_timestamp_unit import DatasetTimestampUnit
from ..models.dataset_type import DatasetType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Dataset")


@_attrs_define
class Dataset:
    """A dataset's own metadata — not its data. `currentVersionId` is what a prepare against
    `exchangeId: user` reads by default; see `DatasetVersion` for what a version carries.

    `from`/`to`/`cadence`/`timestampUnit`/`bytes`/`rows`/`gaps`/`largestGapSteps` mirror that
    current version's own discovered range, cadence, timestamp unit and metrics, so you don't
    need a second call to `GET /datasets/{datasetId}/uploads/{uploadId}` just to see what a
    dataset covers.

        Attributes:
            dataset_id (str): Opaque id, returned by `POST /datasets`. Example: ds_3f9a1c2e7b0d4a5f.
            name (str): Unique among your datasets. Example: My BTC ticks.
            type_ (DatasetType): `ticker` for an upload or a `dex` import with no `cadence` requested (native per-trade
                data). `klines` for a `dex` import that requested a candle `cadence` — pre-aggregated
                bars rather than raw ticks. Purely informational; both shapes are read the same way.
                 Example: ticker.
            instrument (str): Exchange instrument identifier (e.g. a currency pair) Example: BTC/USDT.
            created_at (datetime.datetime): When the dataset was created. Example: 2026-08-20T09:00:00Z.
            status (DatasetStatus): * `ready` — `currentVersionId` is set; `from`/`to`/`cadence`/`bytes`/`rows`/`gaps`/
                  `largestGapSteps` describe it.
                * `failed` — the most recent upload/import attempt failed. `currentVersionId` and the
                  fields above are absent — there is nothing to read yet. See `error`.
                * `pending` — nothing has ever been attempted (just created, or an upload was never
                  finalized).
                 Example: ready.
            current_version_id (str | Unset): The id of the most recently finalized, successfully ingested version. Absent
                until at
                least one upload has finished ingesting.
                 Example: dsv_8e2b4f19c6a03d7e.
            deleted_at (datetime.datetime | Unset): When you deleted this dataset. Only ever present in `GET
                /datasets?includeDeleted=true`,
                and only on datasets you have deleted.
            updated_at (datetime.datetime | Unset): When `currentVersionId` last changed. Absent until it has a value.
                Example: 2026-08-20T09:04:12Z.
            from_ (datetime.datetime | Unset): Start of `currentVersionId`'s own data range, as discovered at ingest time.
                Absent
                until a version exists.
                 Example: 2026-03-01T00:00:00Z.
            to (datetime.datetime | Unset): End of `currentVersionId`'s own data range, as discovered at ingest time. Absent
                until
                a version exists.
                 Example: 2026-03-08T00:00:00Z.
            cadence (str | Unset): `currentVersionId`'s own discovered cadence — a fixed grid (e.g. `1s`, `1m`, `1h`) or
                `rt` (see `DatasetVersion.cadence`). Absent until a version exists.
                 Example: 1m.
            timestamp_unit (DatasetTimestampUnit | Unset): `currentVersionId`'s own timestamp unit (see
                `DatasetVersion.timestampUnit`) — decode
                the `timestamp` column of `dataUrl`'s file accordingly. Present only when `status` is
                `ready`.
                 Example: iso.
            bytes_ (int | Unset): Size of `currentVersionId`'s own stored file. Present only when `status` is `ready` —
                see `DatasetVersion.bytes` for what it measures exactly.
                 Example: 4831022.
            rows (int | Unset): `currentVersionId`'s own row count. Present only when `status` is `ready`. Example: 86400.
            gaps (int | Unset): `currentVersionId`'s own gap count at its discovered cadence. Present only when `status` is
                `ready`.
            largest_gap_steps (int | Unset): `currentVersionId`'s own largest gap, in units of its discovered cadence step.
                Present only when `status` is `ready`.
            error (str | Unset): A human-readable reason the most recent upload/import attempt failed. Present only
                when `status` is `failed`.
                 Example: line 3: column 'close' is not a number: not-a-number.
    """

    dataset_id: str
    name: str
    type_: DatasetType
    instrument: str
    created_at: datetime.datetime
    status: DatasetStatus
    current_version_id: str | Unset = UNSET
    deleted_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    from_: datetime.datetime | Unset = UNSET
    to: datetime.datetime | Unset = UNSET
    cadence: str | Unset = UNSET
    timestamp_unit: DatasetTimestampUnit | Unset = UNSET
    bytes_: int | Unset = UNSET
    rows: int | Unset = UNSET
    gaps: int | Unset = UNSET
    largest_gap_steps: int | Unset = UNSET
    error: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dataset_id = self.dataset_id

        name = self.name

        type_ = self.type_.value

        instrument = self.instrument

        created_at = self.created_at.isoformat()

        status = self.status.value

        current_version_id = self.current_version_id

        deleted_at: str | Unset = UNSET
        if not isinstance(self.deleted_at, Unset):
            deleted_at = self.deleted_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        from_: str | Unset = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.isoformat()

        to: str | Unset = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.isoformat()

        cadence = self.cadence

        timestamp_unit: str | Unset = UNSET
        if not isinstance(self.timestamp_unit, Unset):
            timestamp_unit = self.timestamp_unit.value

        bytes_ = self.bytes_

        rows = self.rows

        gaps = self.gaps

        largest_gap_steps = self.largest_gap_steps

        error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "datasetId": dataset_id,
                "name": name,
                "type": type_,
                "instrument": instrument,
                "createdAt": created_at,
                "status": status,
            }
        )
        if current_version_id is not UNSET:
            field_dict["currentVersionId"] = current_version_id
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if cadence is not UNSET:
            field_dict["cadence"] = cadence
        if timestamp_unit is not UNSET:
            field_dict["timestampUnit"] = timestamp_unit
        if bytes_ is not UNSET:
            field_dict["bytes"] = bytes_
        if rows is not UNSET:
            field_dict["rows"] = rows
        if gaps is not UNSET:
            field_dict["gaps"] = gaps
        if largest_gap_steps is not UNSET:
            field_dict["largestGapSteps"] = largest_gap_steps
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dataset_id = d.pop("datasetId")

        name = d.pop("name")

        type_ = DatasetType(d.pop("type"))

        instrument = d.pop("instrument")

        created_at = isoparse(d.pop("createdAt"))

        status = DatasetStatus(d.pop("status"))

        current_version_id = d.pop("currentVersionId", UNSET)

        _deleted_at = d.pop("deletedAt", UNSET)
        deleted_at: datetime.datetime | Unset
        if isinstance(_deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = isoparse(_deleted_at)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        _from_ = d.pop("from", UNSET)
        from_: datetime.datetime | Unset
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = isoparse(_from_)

        _to = d.pop("to", UNSET)
        to: datetime.datetime | Unset
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = isoparse(_to)

        cadence = d.pop("cadence", UNSET)

        _timestamp_unit = d.pop("timestampUnit", UNSET)
        timestamp_unit: DatasetTimestampUnit | Unset
        if isinstance(_timestamp_unit, Unset):
            timestamp_unit = UNSET
        else:
            timestamp_unit = DatasetTimestampUnit(_timestamp_unit)

        bytes_ = d.pop("bytes", UNSET)

        rows = d.pop("rows", UNSET)

        gaps = d.pop("gaps", UNSET)

        largest_gap_steps = d.pop("largestGapSteps", UNSET)

        error = d.pop("error", UNSET)

        dataset = cls(
            dataset_id=dataset_id,
            name=name,
            type_=type_,
            instrument=instrument,
            created_at=created_at,
            status=status,
            current_version_id=current_version_id,
            deleted_at=deleted_at,
            updated_at=updated_at,
            from_=from_,
            to=to,
            cadence=cadence,
            timestamp_unit=timestamp_unit,
            bytes_=bytes_,
            rows=rows,
            gaps=gaps,
            largest_gap_steps=largest_gap_steps,
            error=error,
        )

        dataset.additional_properties = d
        return dataset

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
