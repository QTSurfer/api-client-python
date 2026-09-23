from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dataset_import_created_status import DatasetImportCreatedStatus

T = TypeVar("T", bound="DatasetImportCreated")


@_attrs_define
class DatasetImportCreated:
    """The response to `POST /datasets/imports` — the dataset now exists, and its fetch has started.

    Attributes:
        dataset_id (str): Opaque id of the newly created dataset — same id space as `POST /datasets`. Example:
            ds_3f9a1c2e7b0d4a5f.
        import_id (str): Identifies this import. Pass to `GET /datasets/{datasetId}/imports/{importId}` to poll
            it — there is no separate "finalize" step the way an upload has.
             Example: imp_01j9z1x2y3z4a5b6c7d8e9f0g1.
        job_id (str): The fetch/ingest job id. Example: dataset-
            import:00000000-.../ds_3f9a1c2e7b0d4a5f:imp_01j9z1x2y3z4a5b6c7d8e9f0g1.
        status (DatasetImportCreatedStatus): Always `fetching` in this response — the fetch has only just started.
            Example: fetching.
    """

    dataset_id: str
    import_id: str
    job_id: str
    status: DatasetImportCreatedStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dataset_id = self.dataset_id

        import_id = self.import_id

        job_id = self.job_id

        status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "datasetId": dataset_id,
                "importId": import_id,
                "jobId": job_id,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dataset_id = d.pop("datasetId")

        import_id = d.pop("importId")

        job_id = d.pop("jobId")

        status = DatasetImportCreatedStatus(d.pop("status"))

        dataset_import_created = cls(
            dataset_id=dataset_id,
            import_id=import_id,
            job_id=job_id,
            status=status,
        )

        dataset_import_created.additional_properties = d
        return dataset_import_created

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
