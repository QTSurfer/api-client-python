from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.instrument_detail import InstrumentDetail
    from ..models.instrument_links import InstrumentLinks
    from ..models.instrument_list_meta import InstrumentListMeta


T = TypeVar("T", bound="InstrumentListResponse")


@_attrs_define
class InstrumentListResponse:
    """HAL-style response envelope for the instruments listing

    Attributes:
        data (list[InstrumentDetail]): The list of instruments for the segment
        meta (InstrumentListMeta): Metadata describing the instruments listing
        field_links (InstrumentLinks): HAL `_links` — segment discovery for the instruments listing
    """

    data: list[InstrumentDetail]
    meta: InstrumentListMeta
    field_links: InstrumentLinks
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        meta = self.meta.to_dict()

        field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "meta": meta,
                "_links": field_links,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.instrument_detail import InstrumentDetail
        from ..models.instrument_links import InstrumentLinks
        from ..models.instrument_list_meta import InstrumentListMeta

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = InstrumentDetail.from_dict(data_item_data)

            data.append(data_item)

        meta = InstrumentListMeta.from_dict(d.pop("meta"))

        field_links = InstrumentLinks.from_dict(d.pop("_links"))

        instrument_list_response = cls(
            data=data,
            meta=meta,
            field_links=field_links,
        )

        instrument_list_response.additional_properties = d
        return instrument_list_response

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
