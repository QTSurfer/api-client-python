from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.prepare_request_cadence import PrepareRequestCadence
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
            cadence (PrepareRequestCadence | Unset): Output bar cadence for the prepared range. Defaults to the publisher's
                native cadence (`1s`); coarser cadences are produced on demand via
                resampling and stored alongside the native blob in cache. Coarser-than-
                source values must be exact multiples of the source cadence — invalid
                labels return `400`.
                 Default: PrepareRequestCadence.VALUE_0.
    """

    from_: str
    to: str
    instrument: str | Unset = UNSET
    dataset_id: str | Unset = UNSET
    dataset_version_id: str | Unset = UNSET
    cadence: PrepareRequestCadence | Unset = PrepareRequestCadence.VALUE_0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_ = self.from_

        to = self.to

        instrument = self.instrument

        dataset_id = self.dataset_id

        dataset_version_id = self.dataset_version_id

        cadence: str | Unset = UNSET
        if not isinstance(self.cadence, Unset):
            cadence = self.cadence.value

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

        _cadence = d.pop("cadence", UNSET)
        cadence: PrepareRequestCadence | Unset
        if isinstance(_cadence, Unset):
            cadence = UNSET
        else:
            cadence = PrepareRequestCadence(_cadence)

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
