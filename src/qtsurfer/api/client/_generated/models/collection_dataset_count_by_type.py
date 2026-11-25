from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CollectionDatasetCountByType")


@_attrs_define
class CollectionDatasetCountByType:
    """The same datasets counted by their `type` (`ticker`, `klines`): a key for each type that
    has at least one dataset, the count as its value. Absent when the collection has no
    datasets. The keys come in no particular order.

        Example:
            {'klines': 2, 'ticker': 1}

    """

    additional_properties: dict[str, int] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        collection_dataset_count_by_type = cls()

        collection_dataset_count_by_type.additional_properties = d
        return collection_dataset_count_by_type

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> int:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: int) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
