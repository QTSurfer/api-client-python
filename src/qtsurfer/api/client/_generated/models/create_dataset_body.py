from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateDatasetBody")


@_attrs_define
class CreateDatasetBody:
    """
    Attributes:
        name (str): A name unique among your datasets. `409` if already taken. Example: My BTC ticks.
        instrument (str): Exchange instrument identifier (e.g. a currency pair) Example: BTC/USDT.
        collection_id (None | str | Unset): Optional. The collection to create the dataset in; `null`, or leaving it
            out,
            creates it at the root. An id that is not one of your collections is `404`, and
            nothing is created. The `201` carries `collectionId` only when you sent one.
             Example: dc_3f9a1c2e7b0d4a5f.
    """

    name: str
    instrument: str
    collection_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        instrument = self.instrument

        collection_id: None | str | Unset
        if isinstance(self.collection_id, Unset):
            collection_id = UNSET
        else:
            collection_id = self.collection_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "instrument": instrument,
            }
        )
        if collection_id is not UNSET:
            field_dict["collectionId"] = collection_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        instrument = d.pop("instrument")

        def _parse_collection_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        collection_id = _parse_collection_id(d.pop("collectionId", UNSET))

        create_dataset_body = cls(
            name=name,
            instrument=instrument,
            collection_id=collection_id,
        )

        create_dataset_body.additional_properties = d
        return create_dataset_body

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
