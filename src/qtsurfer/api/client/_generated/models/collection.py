from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.collection_dataset_count_by_type import CollectionDatasetCountByType


T = TypeVar("T", bound="Collection")


@_attrs_define
class Collection:
    """A folder of datasets. A dataset is in at most one collection, and a collection holds
    datasets of any `type`.

        Attributes:
            collection_id (str): Opaque id, returned by `POST /collections`. Example: dc_3f9a1c2e7b0d4a5f.
            name (str): Unique among your collections, compared as written. Example: Majors.
            created_at (datetime.datetime):  Example: 2026-11-23T09:00:00Z.
            updated_at (datetime.datetime): When the collection's `name` or `description` last changed. Example:
                2026-11-23T09:20:00Z.
            dataset_count (int): How many datasets are in the collection now. A dataset you have deleted does not count.
                Example: 3.
            description (str | Unset): Absent when the collection has none. Example: BTC and ETH, one-minute bars.
            dataset_count_by_type (CollectionDatasetCountByType | Unset): The same datasets counted by their `type`
                (`ticker`, `klines`): a key for each type that
                has at least one dataset, the count as its value. Absent when the collection has no
                datasets. The keys come in no particular order.
                 Example: {'klines': 2, 'ticker': 1}.
    """

    collection_id: str
    name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    dataset_count: int
    description: str | Unset = UNSET
    dataset_count_by_type: CollectionDatasetCountByType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collection_id = self.collection_id

        name = self.name

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        dataset_count = self.dataset_count

        description = self.description

        dataset_count_by_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dataset_count_by_type, Unset):
            dataset_count_by_type = self.dataset_count_by_type.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collectionId": collection_id,
                "name": name,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "datasetCount": dataset_count,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if dataset_count_by_type is not UNSET:
            field_dict["datasetCountByType"] = dataset_count_by_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.collection_dataset_count_by_type import CollectionDatasetCountByType

        d = dict(src_dict)
        collection_id = d.pop("collectionId")

        name = d.pop("name")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        dataset_count = d.pop("datasetCount")

        description = d.pop("description", UNSET)

        _dataset_count_by_type = d.pop("datasetCountByType", UNSET)
        dataset_count_by_type: CollectionDatasetCountByType | Unset
        if isinstance(_dataset_count_by_type, Unset):
            dataset_count_by_type = UNSET
        else:
            dataset_count_by_type = CollectionDatasetCountByType.from_dict(_dataset_count_by_type)

        collection = cls(
            collection_id=collection_id,
            name=name,
            created_at=created_at,
            updated_at=updated_at,
            dataset_count=dataset_count,
            description=description,
            dataset_count_by_type=dataset_count_by_type,
        )

        collection.additional_properties = d
        return collection

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
