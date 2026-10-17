from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dataset_import_cex_request_data_type import DatasetImportCexRequestDataType
from ..models.dataset_import_cex_request_segment import DatasetImportCexRequestSegment

T = TypeVar("T", bound="DatasetImportCexRequest")


@_attrs_define
class DatasetImportCexRequest:
    """The `cex` source's own fields — required when `type` is `cex`. They name a market the way
    `GET /exchanges` and the instruments routes do: `exchange` is the `id` of a centralized
    exchange, `segment` one of its `segments`.

        Example:
            {'exchange': 'binance', 'segment': 'spot', 'dataType': 'klines'}

        Attributes:
            exchange (str): The id of a centralized exchange (`venueType` `cex`) of `GET /exchanges`, lower-case.
                A decentralized exchange's id is `400`: import its pools with `type: dex`.
                 Example: binance.
            segment (DatasetImportCexRequestSegment): The market segment, one of the exchange's `segments`. `spot` is the
                only segment a
                `cex` import takes today, which matches `instrument` being a plain spot pair.
                 Example: spot.
            data_type (DatasetImportCexRequestDataType): What to import, and the resulting dataset's `type`: `ticker` — the
                exchange's ticker
                series — or `klines` — its aggregated bars (open, high, low, close and volume).
                 Example: klines.
    """

    exchange: str
    segment: DatasetImportCexRequestSegment
    data_type: DatasetImportCexRequestDataType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exchange = self.exchange

        segment = self.segment.value

        data_type = self.data_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "exchange": exchange,
                "segment": segment,
                "dataType": data_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        exchange = d.pop("exchange")

        segment = DatasetImportCexRequestSegment(d.pop("segment"))

        data_type = DatasetImportCexRequestDataType(d.pop("dataType"))

        dataset_import_cex_request = cls(
            exchange=exchange,
            segment=segment,
            data_type=data_type,
        )

        dataset_import_cex_request.additional_properties = d
        return dataset_import_cex_request

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
