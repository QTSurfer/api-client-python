from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.dataset_status import DatasetStatus
from ..models.dataset_timestamp_unit import DatasetTimestampUnit
from ..models.dataset_type import DatasetType
from ..models.dataset_with_links_data_format import DatasetWithLinksDataFormat
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dataset_meta import DatasetMeta
    from ..models.dataset_with_links_links import DatasetWithLinksLinks


T = TypeVar("T", bound="DatasetWithLinks")


@_attrs_define
class DatasetWithLinks:
    """A `Dataset` plus a self link. Returned by `GET /datasets/{datasetId}`.

    Attributes:
        dataset_id (str): Opaque id, returned by `POST /datasets`. Example: ds_3f9a1c2e7b0d4a5f.
        name (str): Unique among your datasets, whatever collection each is in. Example: My BTC ticks.
        type_ (DatasetType): What the rows of the current version are, decided when the version became `ready`. An
            import that knows what it fetched says so: a `cex` import is its `dataType`, a `dex`
            import of candles is `klines`. Everything else (an upload, a `dex` import of on-chain
            swaps) is read from the data: `ticker` when any row carries an order book (`bid`,
            `bidSize`, `ask`, `askSize`), or when there is only a price, or only some of
            `open`/`high`/`low`/`close`; `klines` when there is no book and `open`, `high`, `low`
            and `close` are on every row (candles). A file with no book whose `high` and `low`
            hardly ever change, or whose opens do not follow the closes before them (the
            exchange's 24-hour figures), stays `ticker`. A `kline` backtest needs `klines`; a
            `ticker` one takes either. Before the first version is
            `ready` it is only the label of the way the dataset was created (`ticker` for an
            upload, `klines` for an import that asked for candles). Datasets stored before this
            rule keep the `type` they had.
             Example: klines.
        instrument (str): Exchange instrument identifier (e.g. a currency pair) Example: BTC/USDT.
        created_at (datetime.datetime): When the dataset was created. Example: 2026-08-20T09:00:00Z.
        status (DatasetStatus): * `ready` — `currentVersionId` is set; `from`/`to`/`cadence`/`bytes`/`rows`/`gaps`/
              `largestGapSteps` describe it.
            * `failed` — the most recent upload/import attempt failed. `currentVersionId` and the
              fields above are absent — there is nothing to read yet. See `error`.
            * `pending` — nothing has ever been attempted (just created, or an upload was never
              finalized).
             Example: ready.
        collection_id (str | Unset): The collection the dataset is in. Absent when it is at the root, never `null`. It
            changes with `PATCH /datasets/{datasetId}`, and goes away when the collection is deleted.
             Example: dc_3f9a1c2e7b0d4a5f.
        meta (DatasetMeta | Unset): How the dataset came to be: a flat map of text to text, written once when the
            dataset
            is created and never changed afterwards. Always present, `{}` when nothing was recorded
            (an upload, or a dataset created before this field existed). It is information for
            whoever looks at the dataset, not something the API decides anything from.

            An import records what it was asked for, under keys that begin with `import.`
            (`import.type`, `import.cadence`, `import.from`, `import.to`, the range requested),
            `dex.` (`dex.network`, `dex.contract`, `dex.id`, `dex.version`, `dex.factory`) or `cex.`
            (`cex.exchange`, `cex.segment`, `cex.data_type`). A key with no value is left out. The
            keys the caller sent with the import (`pool.*`, `user.*`, see `DatasetImportRequest`)
            come back beside them.
             Example: {'import.type': 'dex', 'import.cadence': '1s', 'import.from': '2026-11-16T00:25:02Z', 'import.to':
            '2026-11-16T10:30:00Z', 'dex.network': 'solana', 'dex.contract': '6nwmQSgHWtRfXw9xqQM3hseyKzWrQq2gzamoSbjKqs32',
            'pool.name': 'FiveM / SOL'}.
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
        data_url (str | Unset): Presigned GET URL to the current version's stored file — see `dataFormat` for
            which format it's actually in. Present only once the current version's status is
            `ready`. It is time-limited, so read the dataset again for a fresh one. It is meant to
            last through a viewing session in which a DuckDB-WASM/`lastra-ts`-style reader issues
            HTTP range requests against it lazily, not just one shot like a browser upload.
             Example: https://storage.qtsurfer.com/00000000-
            .../ds_3f9a1c2e7b0d4a5f/dsv_8e2b4f19c6a03d7e/ticker_BTC_USDT_1700000000000_1700086400000_1m.lastra?....
        data_format (DatasetWithLinksDataFormat | Unset): Which format `dataUrl` is actually in — check this rather than
            assuming it
            matches how you uploaded it. `lastra` — our native columnar format — for a CSV (or
            gzip/zip of one) upload, always converted on ingest, or for a lastra upload,
            stored as it is (the value alone doesn't tell you which). `parquet` for a parquet
            upload, also stored as it is.
             Example: lastra.
        field_links (DatasetWithLinksLinks | Unset):
    """

    dataset_id: str
    name: str
    type_: DatasetType
    instrument: str
    created_at: datetime.datetime
    status: DatasetStatus
    collection_id: str | Unset = UNSET
    meta: DatasetMeta | Unset = UNSET
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
    data_url: str | Unset = UNSET
    data_format: DatasetWithLinksDataFormat | Unset = UNSET
    field_links: DatasetWithLinksLinks | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dataset_id = self.dataset_id

        name = self.name

        type_ = self.type_.value

        instrument = self.instrument

        created_at = self.created_at.isoformat()

        status = self.status.value

        collection_id = self.collection_id

        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

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

        data_url = self.data_url

        data_format: str | Unset = UNSET
        if not isinstance(self.data_format, Unset):
            data_format = self.data_format.value

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

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
        if collection_id is not UNSET:
            field_dict["collectionId"] = collection_id
        if meta is not UNSET:
            field_dict["meta"] = meta
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
        if data_url is not UNSET:
            field_dict["dataUrl"] = data_url
        if data_format is not UNSET:
            field_dict["dataFormat"] = data_format
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataset_meta import DatasetMeta
        from ..models.dataset_with_links_links import DatasetWithLinksLinks

        d = dict(src_dict)
        dataset_id = d.pop("datasetId")

        name = d.pop("name")

        type_ = DatasetType(d.pop("type"))

        instrument = d.pop("instrument")

        created_at = isoparse(d.pop("createdAt"))

        status = DatasetStatus(d.pop("status"))

        collection_id = d.pop("collectionId", UNSET)

        _meta = d.pop("meta", UNSET)
        meta: DatasetMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = DatasetMeta.from_dict(_meta)

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

        data_url = d.pop("dataUrl", UNSET)

        _data_format = d.pop("dataFormat", UNSET)
        data_format: DatasetWithLinksDataFormat | Unset
        if isinstance(_data_format, Unset):
            data_format = UNSET
        else:
            data_format = DatasetWithLinksDataFormat(_data_format)

        _field_links = d.pop("_links", UNSET)
        field_links: DatasetWithLinksLinks | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = DatasetWithLinksLinks.from_dict(_field_links)

        dataset_with_links = cls(
            dataset_id=dataset_id,
            name=name,
            type_=type_,
            instrument=instrument,
            created_at=created_at,
            status=status,
            collection_id=collection_id,
            meta=meta,
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
            data_url=data_url,
            data_format=data_format,
            field_links=field_links,
        )

        dataset_with_links.additional_properties = d
        return dataset_with_links

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
