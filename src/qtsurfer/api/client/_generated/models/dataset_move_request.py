from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="DatasetMoveRequest")


@_attrs_define
class DatasetMoveRequest:
    """The body of `PATCH /datasets/{datasetId}`: exactly one field, `collectionId`. A body
    without it, or with any other field, is `400`.

        Attributes:
            collection_id (None | str): The collection to move the dataset into, or `null` to take it out of its collection
                and back to the root. Example: dc_3f9a1c2e7b0d4a5f.
    """

    collection_id: None | str

    def to_dict(self) -> dict[str, Any]:
        collection_id: None | str
        collection_id = self.collection_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "collectionId": collection_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_collection_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        collection_id = _parse_collection_id(d.pop("collectionId"))

        dataset_move_request = cls(
            collection_id=collection_id,
        )

        return dataset_move_request
