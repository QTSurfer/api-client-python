from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.dataset_import_request_cadence import DatasetImportRequestCadence
from ..models.dataset_import_request_type import DatasetImportRequestType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dataset_import_cex_request import DatasetImportCexRequest
    from ..models.dataset_import_dex_request import DatasetImportDexRequest
    from ..models.dataset_import_request_meta import DatasetImportRequestMeta


T = TypeVar("T", bound="DatasetImportRequest")


@_attrs_define
class DatasetImportRequest:
    """`POST /datasets/imports`'s request body. A common block plus one type-specific block,
    selected by `type`: `dex` (block `dex`) or `cex` (block `cex`), the two `venueType`s of
    `GET /exchanges`.

        Attributes:
            name (str): A name unique among your datasets. `409` if already taken. Example: weth-usdc-week.
            instrument (str): Exchange instrument identifier (e.g. a currency pair) Example: BTC/USDT.
            from_ (datetime.datetime): Start of the range to fetch, inclusive. Must be before `to`. Example:
                2026-10-27T00:00:00Z.
            to (datetime.datetime): End of the range to fetch, exclusive. The total span is capped by your tier — a
                request wider than that ceiling is `400`, regardless of source type.
                 Example: 2026-10-27T06:00:00Z.
            type_ (DatasetImportRequestType): The kind of venue to import from, the same two values as the `venueType` of
                `GET /exchanges`: `dex` — a pool/pair's own on-chain market (block `dex`) — or `cex` —
                a centralized exchange's market history (block `cex`).
                 Example: cex.
            collection_id (None | str | Unset): Optional. The collection to create the dataset in; `null`, or leaving it
                out, creates
                it at the root. An id that is not one of your collections is `404`, answered before the
                import is queued and before anything is counted against your plan. The `202` carries
                `collectionId` only when you sent one.
                 Example: dc_3f9a1c2e7b0d4a5f.
            cadence (DatasetImportRequestCadence | Unset): Optional; what it means, and what it accepts, depends on `type`.
                Any other value is
                `400`. A cadence your plan does not include is `402` (the "Cadences by plan" section of the Backtests guide
                lists them).

                * `dex` — candles at that width (the resulting dataset's `type` is `klines`), built from
                  the nearest width the source serves. Omitted/blank = the plan's default; on a plan
                  that includes the native rate of a source, omitted keeps native per-trade event
                  cadence: each swap at its own timestamp, so the resulting version's `cadence` is `rt`
                  unless the swaps happen to sit on a fixed grid (see `DatasetVersion.cadence`).
                  Not every network supports candles — an unsupported combination fails
                  asynchronously, not at request time (see `DatasetImportState.error`). On `solana`,
                  which has candles only, omitted is the plan's default as candles on every plan.
                * `cex` — one of `1s`, `5s`, `1m`, `3m`, `5m`, `15m`, `30m`, `1h`, `2h`, `4h`, `8h`,
                  `12h`, `1d`, `1w`, `1q`, whether `dataType` is `ticker` or `klines`. Omitted = the
                  plan's default; on a plan that includes the native rate of a source, the finest
                  cadence every part of the range holds.

                For `cex` the bars are built from the finest data every part of the range holds. A
                `cadence` finer than that, or not an exact multiple of it, fails the import
                asynchronously (`failed`; the `error` names the finest cadence the range holds) rather
                than returning a dataset with a different cadence from the one asked for. So a range
                whose history changes cadence part-way (from `1m` to `1s`, say) comes out entirely at
                the coarser one when the range decides it (a plan that includes the native rate, no
                `cadence`): the dataset has no gap that is only a
                change of cadence.
            dex (DatasetImportDexRequest | Unset): The `dex` source's own fields — required when `type` is `dex`.
                `id`/`version` are required
                for a plain (native-cadence) import; both are ignored if the top-level `cadence` requested
                pre-aggregated candles instead, since that path needs neither a protocol nor a version
                distinction.
                 Example: {'network': 'ethereum', 'id': 'uniswap', 'version': 'v3', 'contract':
                '0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640'}.
            cex (DatasetImportCexRequest | Unset): The `cex` source's own fields — required when `type` is `cex`. They name
                a market the way
                `GET /exchanges` and the instruments routes do: `exchange` is the `id` of a centralized
                exchange, `segment` one of its `segments`.
                 Example: {'exchange': 'binance', 'segment': 'spot', 'dataType': 'klines'}.
            meta (DatasetImportRequestMeta | Unset): Optional. Keys of your own to keep on the dataset, returned as `meta`
                of the `Dataset`
                beside the ones the import records itself. Two namespaces are yours: `pool.*`, a note
                about the pool the import is for (by convention `pool.id`, `pool.name`, `pool.dex`,
                `pool.reserve_usd`, `pool.created_at`), and `user.*`, any label you like. A key of the
                platform's (`import.*`, `dex.*`, `cex.*`) or of any other namespace is `400`.

                A key is lower-case letters, digits and `_`, in parts separated by `.`, at most 64
                characters. A value is a non-empty text of at most 256 characters with no control
                characters. At most 16 keys, and the whole of what is kept (your keys and the ones the
                import adds) at most 32 keys and 4096 bytes of JSON. Anything over a limit is `400`; the
                import is not created. `meta` is not taken by `POST /datasets`.
                 Example: {'pool.name': 'FiveM / SOL', 'pool.dex': 'PumpSwap', 'user.label': 'week one'}.
    """

    name: str
    instrument: str
    from_: datetime.datetime
    to: datetime.datetime
    type_: DatasetImportRequestType
    collection_id: None | str | Unset = UNSET
    cadence: DatasetImportRequestCadence | Unset = UNSET
    dex: DatasetImportDexRequest | Unset = UNSET
    cex: DatasetImportCexRequest | Unset = UNSET
    meta: DatasetImportRequestMeta | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        instrument = self.instrument

        from_ = self.from_.isoformat()

        to = self.to.isoformat()

        type_ = self.type_.value

        collection_id: None | str | Unset
        if isinstance(self.collection_id, Unset):
            collection_id = UNSET
        else:
            collection_id = self.collection_id

        cadence: str | Unset = UNSET
        if not isinstance(self.cadence, Unset):
            cadence = self.cadence.value

        dex: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dex, Unset):
            dex = self.dex.to_dict()

        cex: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cex, Unset):
            cex = self.cex.to_dict()

        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

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
        if collection_id is not UNSET:
            field_dict["collectionId"] = collection_id
        if cadence is not UNSET:
            field_dict["cadence"] = cadence
        if dex is not UNSET:
            field_dict["dex"] = dex
        if cex is not UNSET:
            field_dict["cex"] = cex
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataset_import_cex_request import DatasetImportCexRequest
        from ..models.dataset_import_dex_request import DatasetImportDexRequest
        from ..models.dataset_import_request_meta import DatasetImportRequestMeta

        d = dict(src_dict)
        name = d.pop("name")

        instrument = d.pop("instrument")

        from_ = isoparse(d.pop("from"))

        to = isoparse(d.pop("to"))

        type_ = DatasetImportRequestType(d.pop("type"))

        def _parse_collection_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        collection_id = _parse_collection_id(d.pop("collectionId", UNSET))

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

        _cex = d.pop("cex", UNSET)
        cex: DatasetImportCexRequest | Unset
        if isinstance(_cex, Unset):
            cex = UNSET
        else:
            cex = DatasetImportCexRequest.from_dict(_cex)

        _meta = d.pop("meta", UNSET)
        meta: DatasetImportRequestMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = DatasetImportRequestMeta.from_dict(_meta)

        dataset_import_request = cls(
            name=name,
            instrument=instrument,
            from_=from_,
            to=to,
            type_=type_,
            collection_id=collection_id,
            cadence=cadence,
            dex=dex,
            cex=cex,
            meta=meta,
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
