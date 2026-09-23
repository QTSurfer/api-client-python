from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.dataset_import_request_cadence import DatasetImportRequestCadence
from ..models.dataset_import_request_type import DatasetImportRequestType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dataset_import_dex_request import DatasetImportDexRequest


T = TypeVar("T", bound="DatasetImportRequest")


@_attrs_define
class DatasetImportRequest:
    """`POST /datasets/imports`'s request body. A common block plus one type-specific block,
    selected by `type` — `dex` is the only value today.

        Attributes:
            name (str): A name unique among your datasets. `409` if already taken. Example: weth-usdc-week.
            instrument (str): Exchange instrument identifier (e.g. a currency pair) Example: BTC/USDT.
            from_ (datetime.datetime): Start of the range to fetch, inclusive. Must be before `to`. Example:
                2026-08-01T00:00:00Z.
            to (datetime.datetime): End of the range to fetch, exclusive. The total span is capped by your tier — a
                request wider than that ceiling is `400`, regardless of source type.
                 Example: 2026-08-08T00:00:00Z.
            type_ (DatasetImportRequestType): The source to fetch from. `dex` is the only value today. Example: dex.
            cadence (DatasetImportRequestCadence | Unset): Optional. Omitted/blank keeps native per-trade event cadence —
                each swap at its own
                timestamp, so the resulting version's `cadence` is `rt` unless the swaps happen to sit
                on a fixed grid (see `DatasetVersion.cadence`). Set to `1s`, `1m` or
                `5m` instead to get pre-aggregated candles at that width rather than raw trades (the
                resulting dataset's `type` becomes `klines`); any other value is `400`. Not every
                network supports every cadence — an unsupported combination fails asynchronously, not
                at request time (see `DatasetImportState.error`).
            dex (DatasetImportDexRequest | Unset): The `dex` source's own fields — required when `type` is `dex`.
                `id`/`version` are required
                for a plain (native-cadence) import; both are ignored if the top-level `cadence` requested
                pre-aggregated candles instead, since that path needs neither a protocol nor a version
                distinction.
                 Example: {'network': 'ethereum', 'id': 'uniswap', 'version': 'v3', 'contract':
                '0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640'}.
    """

    name: str
    instrument: str
    from_: datetime.datetime
    to: datetime.datetime
    type_: DatasetImportRequestType
    cadence: DatasetImportRequestCadence | Unset = UNSET
    dex: DatasetImportDexRequest | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        instrument = self.instrument

        from_ = self.from_.isoformat()

        to = self.to.isoformat()

        type_ = self.type_.value

        cadence: str | Unset = UNSET
        if not isinstance(self.cadence, Unset):
            cadence = self.cadence.value

        dex: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dex, Unset):
            dex = self.dex.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "instrument": instrument,
                "from": from_,
                "to": to,
                "type": type_,
            }
        )
        if cadence is not UNSET:
            field_dict["cadence"] = cadence
        if dex is not UNSET:
            field_dict["dex"] = dex

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataset_import_dex_request import DatasetImportDexRequest

        d = dict(src_dict)
        name = d.pop("name")

        instrument = d.pop("instrument")

        from_ = isoparse(d.pop("from"))

        to = isoparse(d.pop("to"))

        type_ = DatasetImportRequestType(d.pop("type"))

        _cadence = d.pop("cadence", UNSET)
        cadence: DatasetImportRequestCadence | Unset
        if isinstance(_cadence, Unset):
            cadence = UNSET
        else:
            cadence = DatasetImportRequestCadence(_cadence)

        _dex = d.pop("dex", UNSET)
        dex: DatasetImportDexRequest | Unset
        if isinstance(_dex, Unset):
            dex = UNSET
        else:
            dex = DatasetImportDexRequest.from_dict(_dex)

        dataset_import_request = cls(
            name=name,
            instrument=instrument,
            from_=from_,
            to=to,
            type_=type_,
            cadence=cadence,
            dex=dex,
        )

        dataset_import_request.additional_properties = d
        return dataset_import_request

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
