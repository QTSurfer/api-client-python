from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DatasetUploadTarget")


@_attrs_define
class DatasetUploadTarget:
    """A presigned destination for uploading a raw dataset file directly to storage.

    Attributes:
        url (str): Presigned URL. `PUT` the file here directly — the CSV or parquet itself, or a `.gz`/`.zip` of it
            (see `createDataset`'s own description) — no `Authorization` header, no other API
            credentials.
             Example: https://storage.qtsurfer.com/uploads/00000000-.../up_1a2b3c4d5e6f7a8b/raw.csv?X-Amz-....
        expires_in_minutes (int): How long `url` stays valid. Example: 15.
    """

    url: str
    expires_in_minutes: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        expires_in_minutes = self.expires_in_minutes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "expiresInMinutes": expires_in_minutes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        expires_in_minutes = d.pop("expiresInMinutes")

        dataset_upload_target = cls(
            url=url,
            expires_in_minutes=expires_in_minutes,
        )

        dataset_upload_target.additional_properties = d
        return dataset_upload_target

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
