from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.dataset_type import DatasetType
from ..models.dataset_with_links_data_format import DatasetWithLinksDataFormat
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dataset_with_links_links import DatasetWithLinksLinks


T = TypeVar("T", bound="DatasetWithLinks")


@_attrs_define
class DatasetWithLinks:
    """A `Dataset` plus a self link. Returned by `GET /datasets/{datasetId}`.

    Attributes:
        dataset_id (str): Opaque id, returned by `POST /datasets`. Example: ds_3f9a1c2e7b0d4a5f.
        name (str): Unique among your datasets. Example: My BTC ticks.
        type_ (DatasetType): Always `ticker` in v1. Example: ticker.
        instrument (str): Exchange instrument identifier (e.g. a currency pair) Example: BTC/USDT.
        created_at (datetime.datetime): When the dataset was created. Example: 2026-08-20T09:00:00Z.
        current_version_id (str | Unset): The id of the most recently finalized, successfully ingested version. Absent
            until at
            least one upload has finished ingesting.
             Example: dsv_8e2b4f19c6a03d7e.
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
        cadence (str | Unset): `currentVersionId`'s own discovered bar cadence (e.g. `1s`, `1m`, `1h`). Absent until a
            version exists.
             Example: 1m.
        data_url (str | Unset): Presigned GET URL to the current version's stored file — see `dataFormat` for
            which format it's actually in. Present only once the current version's status is
            `ready`. Long-lived (day-scale, not permanent): a DuckDB-WASM/`lastra-ts`-style
            reader issues HTTP range requests against it lazily over an extended viewing
            session, not in one shot like a browser upload.
             Example: https://storage.qtsurfer.com/00000000-
            .../ds_3f9a1c2e7b0d4a5f/dsv_8e2b4f19c6a03d7e/ticker_BTC_USDT_1700000000000_1700086400000_1m.lastra?X-Amz-....
        data_format (DatasetWithLinksDataFormat | Unset): Which format `dataUrl` is actually in — check this rather than
            assuming it
            matches how you uploaded it. `lastra` — our native columnar format — for a CSV (or
            gzip/zip of one) upload, always converted on ingest. `parquet` for a parquet
            upload, stored as-is today.
             Example: lastra.
        field_links (DatasetWithLinksLinks | Unset):
    """

    dataset_id: str
    name: str
    type_: DatasetType
    instrument: str
    created_at: datetime.datetime
    current_version_id: str | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    from_: datetime.datetime | Unset = UNSET
    to: datetime.datetime | Unset = UNSET
    cadence: str | Unset = UNSET
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

        current_version_id = self.current_version_id

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
            }
        )
        if current_version_id is not UNSET:
            field_dict["currentVersionId"] = current_version_id
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if cadence is not UNSET:
            field_dict["cadence"] = cadence
        if data_url is not UNSET:
            field_dict["dataUrl"] = data_url
        if data_format is not UNSET:
            field_dict["dataFormat"] = data_format
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataset_with_links_links import DatasetWithLinksLinks

        d = dict(src_dict)
        dataset_id = d.pop("datasetId")

        name = d.pop("name")

        type_ = DatasetType(d.pop("type"))

        instrument = d.pop("instrument")

        created_at = isoparse(d.pop("createdAt"))

        current_version_id = d.pop("currentVersionId", UNSET)

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
            current_version_id=current_version_id,
            updated_at=updated_at,
            from_=from_,
            to=to,
            cadence=cadence,
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
