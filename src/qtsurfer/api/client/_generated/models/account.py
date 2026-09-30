from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.account_links import AccountLinks


T = TypeVar("T", bound="Account")


@_attrs_define
class Account:
    """Your identity and tier limits. No database call behind this one — safe to fetch on every
    page load. Live usage against these limits is a separate resource, `GET /account/usage`,
    deliberately: usage changes on every upload/execution and costs a query to compute, this
    one doesn't.

        Attributes:
            user_id (str): Your account id — the JWT `sub` claim. Example: 00000000-0000-0000-0000-000000000000.
            tier (str): Your current subscription tier. Example: free.
            max_execute (int): Maximum number of strategy executions (and sweeps) you can have running at the same time
                through the API. Starting one past this number is answered with `429`, whose message
                carries the same number. The value already includes any API allowance your plan has.
                 Example: 10.
            max_range_days (int): Maximum length, in days, of the time range of a backtest on one of your own datasets.
                Example: 7.
            max_sweep_cartesian (int): Largest full grid, in parameter combinations, a sweep may run with the `grid`
                sampler.
                A grid with more combinations is refused with `400`; the `random` and `lhs` samplers run
                only their `samples` and are not held to it.
                 Example: 100.
            max_import_range_hours (int): Maximum length, in hours, of the time range of one dataset import from an
                exchange. Example: 6.
            max_datasets (int): Maximum number of active datasets your tier allows. Example: 3.
            max_dataset_bytes (int): Maximum size, in bytes, of a single dataset version as stored, that is the `bytes` of
                its ready version. For a CSV upload that is the converted file, not the file you upload, so estimate from the
                number of rows. The Datasets guide has the details. Example: 52428800.
            max_total_storage_bytes (int): Maximum combined storage, in bytes, across every dataset, strategy-execution
                signal,
                and registered strategy on your account — one shared pool, not a separate cap per
                resource type, since they all compete for the same underlying storage. See `GET
                /account/usage`'s `storageBytesUsed` for your current usage against this number.
                 Example: 104857600.
            field_links (AccountLinks): HAL `_links` for `GET /account`
    """

    user_id: str
    tier: str
    max_execute: int
    max_range_days: int
    max_sweep_cartesian: int
    max_import_range_hours: int
    max_datasets: int
    max_dataset_bytes: int
    max_total_storage_bytes: int
    field_links: AccountLinks
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        tier = self.tier

        max_execute = self.max_execute

        max_range_days = self.max_range_days

        max_sweep_cartesian = self.max_sweep_cartesian

        max_import_range_hours = self.max_import_range_hours

        max_datasets = self.max_datasets

        max_dataset_bytes = self.max_dataset_bytes

        max_total_storage_bytes = self.max_total_storage_bytes

        field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userId": user_id,
                "tier": tier,
                "maxExecute": max_execute,
                "maxRangeDays": max_range_days,
                "maxSweepCartesian": max_sweep_cartesian,
                "maxImportRangeHours": max_import_range_hours,
                "maxDatasets": max_datasets,
                "maxDatasetBytes": max_dataset_bytes,
                "maxTotalStorageBytes": max_total_storage_bytes,
                "_links": field_links,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_links import AccountLinks

        d = dict(src_dict)
        user_id = d.pop("userId")

        tier = d.pop("tier")

        max_execute = d.pop("maxExecute")

        max_range_days = d.pop("maxRangeDays")

        max_sweep_cartesian = d.pop("maxSweepCartesian")

        max_import_range_hours = d.pop("maxImportRangeHours")

        max_datasets = d.pop("maxDatasets")

        max_dataset_bytes = d.pop("maxDatasetBytes")

        max_total_storage_bytes = d.pop("maxTotalStorageBytes")

        field_links = AccountLinks.from_dict(d.pop("_links"))

        account = cls(
            user_id=user_id,
            tier=tier,
            max_execute=max_execute,
            max_range_days=max_range_days,
            max_sweep_cartesian=max_sweep_cartesian,
            max_import_range_hours=max_import_range_hours,
            max_datasets=max_datasets,
            max_dataset_bytes=max_dataset_bytes,
            max_total_storage_bytes=max_total_storage_bytes,
            field_links=field_links,
        )

        account.additional_properties = d
        return account

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
