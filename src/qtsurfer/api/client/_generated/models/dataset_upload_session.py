from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dataset_upload_target import DatasetUploadTarget


T = TypeVar("T", bound="DatasetUploadSession")


@_attrs_define
class DatasetUploadSession:
    """An upload session — an id plus the presigned URL to PUT the raw file to. Returned both by
    `POST /datasets` (as part of the new dataset) and by `POST /datasets/{datasetId}/uploads`
    (on its own, for an existing one).

        Attributes:
            upload_id (str): Identifies this upload session. Pass to
                `POST /datasets/{datasetId}/uploads/{uploadId}/finalize` once the PUT completes.
                 Example: up_1a2b3c4d5e6f7a8b.
            upload (DatasetUploadTarget): A presigned destination for uploading a raw dataset file directly to storage.
    """

    upload_id: str
    upload: DatasetUploadTarget
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        upload_id = self.upload_id

        upload = self.upload.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uploadId": upload_id,
                "upload": upload,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataset_upload_target import DatasetUploadTarget

        d = dict(src_dict)
        upload_id = d.pop("uploadId")

        upload = DatasetUploadTarget.from_dict(d.pop("upload"))

        dataset_upload_session = cls(
            upload_id=upload_id,
            upload=upload,
        )

        dataset_upload_session.additional_properties = d
        return dataset_upload_session

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
