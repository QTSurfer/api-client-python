from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PrepareRequest")


@_attrs_define
class PrepareRequest:
    """Two shapes, chosen by the `exchangeId` path segment. Against a managed exchange,
    `instrument` is required and `datasetId`/`datasetVersionId` are ignored. Against the
    reserved `exchangeId: user`, send `datasetId` instead of `instrument` — `instrument` is
    ignored there, since it comes from the dataset itself.

        Example:
            {'instrument': 'BTC/USDT', 'from': '2024-12-13T00:00:00Z', 'to': '2024-12-14T00:00:00Z', 'cadence': '1m'}

        Attributes:
            from_ (str): Start date for the preparation process. Supports the following formats:
                - ISO-8601 (e.g. 2024-12-14T23:59:59Z)
                - ISO DATE (e.g. 2024-12-14)
                - BASIC ISO DATE (e.g., 20241214)
                 Example: 2024-12-13T00:00:00Z.
            to (str): End date for the preparation process. Supports the following formats:
                - ISO-8601 (e.g. 2024-12-14T23:59:59Z)
                - ISO DATE (e.g. 2024-12-14)
                - BASIC ISO DATE (e.g., 20241214)
                 Example: 2024-12-14.
            instrument (str | Unset): Exchange instrument identifier (e.g. a currency pair) Example: BTC/USDT.
            dataset_id (str | Unset): Only for `exchangeId: user`: the id of a dataset created via `POST /datasets`, in
                place
                of `instrument`. Ignored against a managed exchange.
                 Example: ds_3f9a1c2e7b0d4a5f.
            dataset_version_id (str | Unset): Only for `exchangeId: user`, and optional even then: pins a specific past
                version of
                the dataset instead of its current one. Defaults to the dataset's current version.
                 Example: dsv_8e2b4f19c6a03d7e.
            cadence (str | Unset): Output bar cadence for the prepared range. Coarser cadences are produced on demand by
                resampling the source and stored alongside the native blob in cache. A target finer
                than the source, or not an exact multiple of it, returns `400`. What's accepted, and
                what omitting it means, depends on the source:

                * Managed exchange, `ticker` or `funding` — one of `1s`, `5s`, `1m`, `3m`, `5m`, `15m`,
                  `30m`, `1h`, `2h`, `4h`, `8h`, `12h`, `1d`, `1w`, `1q`; any other label returns `400`.
                  Omitted = `1s`, the publisher's native cadence.
                * Managed exchange, `kline` — one of `1s`, `1m`, `5m`, `15m`, `30m`, `1h`, `4h`, `1d`;
                  any other label, including `5s`, `3m` and `8h`, returns `400` and names the accepted
                  ones. Omitted = `1s`. This is the width of the bars a run reads: it is chosen here,
                  once, and the same strategy can be run at several cadences by preparing the range at
                  each.
                * Dataset (`exchangeId: user`) — omitted = the dataset version's own discovered
                  `cadence` (see `DatasetVersion.cadence`), served as-is. Any cadence equal to or
                  coarser than it and an exact multiple of it is accepted, including ones outside the
                  managed-exchange list (e.g. `15s`); an `rt` dataset can be resampled to any fixed
                  cadence.
    """

    from_: str
    to: str
    instrument: str | Unset = UNSET
    dataset_id: str | Unset = UNSET
    dataset_version_id: str | Unset = UNSET
    cadence: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_ = self.from_

        to = self.to

        instrument = self.instrument

        dataset_id = self.dataset_id

        dataset_version_id = self.dataset_version_id

        cadence = self.cadence

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from": from_,
                "to": to,
            }
        )
        if instrument is not UNSET:
            field_dict["instrument"] = instrument
        if dataset_id is not UNSET:
            field_dict["datasetId"] = dataset_id
        if dataset_version_id is not UNSET:
            field_dict["datasetVersionId"] = dataset_version_id
        if cadence is not UNSET:
            field_dict["cadence"] = cadence

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        from_ = d.pop("from")

        to = d.pop("to")

        instrument = d.pop("instrument", UNSET)

        dataset_id = d.pop("datasetId", UNSET)

        dataset_version_id = d.pop("datasetVersionId", UNSET)

        cadence = d.pop("cadence", UNSET)

        prepare_request = cls(
            from_=from_,
            to=to,
            instrument=instrument,
            dataset_id=dataset_id,
            dataset_version_id=dataset_version_id,
            cadence=cadence,
        )

        prepare_request.additional_properties = d
        return prepare_request

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
