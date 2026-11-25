from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dataset_created_type import DatasetCreatedType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dataset_upload_target import DatasetUploadTarget


T = TypeVar("T", bound="DatasetCreated")


@_attrs_define
class DatasetCreated:
    """The metadata available immediately after creating a dataset, plus its first upload
    session — the presigned URL to PUT the file to. Version-derived fields such as
    `createdAt`, `currentVersionId`, range, and cadence are available from `GET /datasets/{datasetId}`
    after the relevant lifecycle stages, not in this creation response.

        Attributes:
            upload_id (str): Identifies this upload session. Pass to
                `POST /datasets/{datasetId}/uploads/{uploadId}/finalize` once the PUT completes.
                 Example: up_1a2b3c4d5e6f7a8b.
            upload (DatasetUploadTarget): A presigned destination for uploading a raw dataset file directly to storage.
            dataset_id (str): Opaque id of the newly created dataset. Example: ds_3f9a1c2e7b0d4a5f.
            name (str): Unique name of the newly created dataset. Example: My BTC ticks.
            type_ (DatasetCreatedType): The label of a dataset that has no data yet, always `ticker` for an upload. The
                dataset's `type` is read from the data once the upload has been ingested (see
                `Dataset.type`): a file of candles is `klines` then.
                 Example: ticker.
            instrument (str): Exchange instrument identifier (e.g. a currency pair) Example: BTC/USDT.
            collection_id (str | Unset): The collection the dataset was created in. Present only when the request named one.
                Example: dc_3f9a1c2e7b0d4a5f.
    """

    upload_id: str
    upload: DatasetUploadTarget
    dataset_id: str
    name: str
    type_: DatasetCreatedType
    instrument: str
    collection_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        upload_id = self.upload_id

        upload = self.upload.to_dict()

        dataset_id = self.dataset_id

        name = self.name

        type_ = self.type_.value

        instrument = self.instrument

        collection_id = self.collection_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uploadId": upload_id,
                "upload": upload,
                "datasetId": dataset_id,
                "name": name,
                "type": type_,
                "instrument": instrument,
            }
        )
        if collection_id is not UNSET:
            field_dict["collectionId"] = collection_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataset_upload_target import DatasetUploadTarget

        d = dict(src_dict)
        upload_id = d.pop("uploadId")

        upload = DatasetUploadTarget.from_dict(d.pop("upload"))

        dataset_id = d.pop("datasetId")

        name = d.pop("name")

        type_ = DatasetCreatedType(d.pop("type"))

        instrument = d.pop("instrument")

        collection_id = d.pop("collectionId", UNSET)

        dataset_created = cls(
            upload_id=upload_id,
            upload=upload,
            dataset_id=dataset_id,
            name=name,
            type_=type_,
            instrument=instrument,
            collection_id=collection_id,
        )

        dataset_created.additional_properties = d
        return dataset_created

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
