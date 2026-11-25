from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_links import AccountLinks
    from ..models.key_scopes import KeyScopes


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
            scopes (KeyScopes): What your API key may do, as a map from a resource to the actions allowed on it. Names are
                lower case: `{ "backtests": ["read", "write", "execute"], "exchanges": ["read"] }`. A scope
                is a resource and an action: a resource is listed only with at least one action, and a key
                with no scope is `{}`. `GET /account` and `POST /auth/token` return the same map for the
                same key. An operation that needs a scope the key does not carry is answered `403` with the
                code `insufficient_scope`, and says which scope it needed.
                 Example: {'backtests': ['read', 'write', 'execute'], 'exchanges': ['read']}.
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
            max_import_range_hours (int): Maximum length, in hours, of the time range of one dataset import of a
                decentralized exchange's pool (`type: dex`). Example: 6.
            max_cex_import_range_hours (int): Maximum length, in hours, of the time range of one dataset import of a
                centralized exchange's history (`type: cex`). It is counted apart from `maxImportRangeHours`. Example: 24.
            max_concurrent_imports (int): Maximum number of dataset imports your account may have in flight at once, queued
                or running, whether of an exchange's history or of a pool. A new import over it is refused with `429` until one
                has finished. Example: 1.
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
            api_key_expires_at (datetime.datetime | None | Unset): When the API key behind this token stops working, UTC.
                Always in the answer; `null` when
                no key expiry applies: a key that never expires, a token issued before this field existed
                (ask for a new one), or a credential that is not an API key. It is the same moment as the
                `key_exp` of `POST /auth/token`. Rotate the key before it: after it, `POST /auth/token`
                answers `401`. A token already issued keeps working until its own expiry.
                 Example: 2026-12-05T10:05:00Z.
            max_cex_history_days (int | Unset): How far back from now, in days, an import of a centralized exchange's
                history (`type: cex`) may start. The largest whole number means as far back as the platform keeps. Absent on a
                platform that has not adopted it. Example: 730.
            max_cex_import_instruments_per_month (int | Unset): How many different instruments of one market (an exchange
                and its segment) your account may import from an exchange's history in a calendar month (UTC). Importing the
                same instrument again in the month costs nothing. The largest whole number means no limit. Absent on a platform
                that has not adopted it. Example: 20.
    """

    user_id: str
    tier: str
    scopes: KeyScopes
    max_execute: int
    max_range_days: int
    max_sweep_cartesian: int
    max_import_range_hours: int
    max_cex_import_range_hours: int
    max_concurrent_imports: int
    max_datasets: int
    max_dataset_bytes: int
    max_total_storage_bytes: int
    field_links: AccountLinks
    api_key_expires_at: datetime.datetime | None | Unset = UNSET
    max_cex_history_days: int | Unset = UNSET
    max_cex_import_instruments_per_month: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        tier = self.tier

        scopes = self.scopes.to_dict()

        max_execute = self.max_execute

        max_range_days = self.max_range_days

        max_sweep_cartesian = self.max_sweep_cartesian

        max_import_range_hours = self.max_import_range_hours

        max_cex_import_range_hours = self.max_cex_import_range_hours

        max_concurrent_imports = self.max_concurrent_imports

        max_datasets = self.max_datasets

        max_dataset_bytes = self.max_dataset_bytes

        max_total_storage_bytes = self.max_total_storage_bytes

        field_links = self.field_links.to_dict()

        api_key_expires_at: None | str | Unset
        if isinstance(self.api_key_expires_at, Unset):
            api_key_expires_at = UNSET
        elif isinstance(self.api_key_expires_at, datetime.datetime):
            api_key_expires_at = self.api_key_expires_at.isoformat()
        else:
            api_key_expires_at = self.api_key_expires_at

        max_cex_history_days = self.max_cex_history_days

        max_cex_import_instruments_per_month = self.max_cex_import_instruments_per_month

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userId": user_id,
                "tier": tier,
                "scopes": scopes,
                "maxExecute": max_execute,
                "maxRangeDays": max_range_days,
                "maxSweepCartesian": max_sweep_cartesian,
                "maxImportRangeHours": max_import_range_hours,
                "maxCexImportRangeHours": max_cex_import_range_hours,
                "maxConcurrentImports": max_concurrent_imports,
                "maxDatasets": max_datasets,
                "maxDatasetBytes": max_dataset_bytes,
                "maxTotalStorageBytes": max_total_storage_bytes,
                "_links": field_links,
            }
        )
        if api_key_expires_at is not UNSET:
            field_dict["apiKeyExpiresAt"] = api_key_expires_at
        if max_cex_history_days is not UNSET:
            field_dict["maxCexHistoryDays"] = max_cex_history_days
        if max_cex_import_instruments_per_month is not UNSET:
            field_dict["maxCexImportInstrumentsPerMonth"] = max_cex_import_instruments_per_month

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_links import AccountLinks
        from ..models.key_scopes import KeyScopes

        d = dict(src_dict)
        user_id = d.pop("userId")

        tier = d.pop("tier")

        scopes = KeyScopes.from_dict(d.pop("scopes"))

        max_execute = d.pop("maxExecute")

        max_range_days = d.pop("maxRangeDays")

        max_sweep_cartesian = d.pop("maxSweepCartesian")

        max_import_range_hours = d.pop("maxImportRangeHours")

        max_cex_import_range_hours = d.pop("maxCexImportRangeHours")

        max_concurrent_imports = d.pop("maxConcurrentImports")

        max_datasets = d.pop("maxDatasets")

        max_dataset_bytes = d.pop("maxDatasetBytes")

        max_total_storage_bytes = d.pop("maxTotalStorageBytes")

        field_links = AccountLinks.from_dict(d.pop("_links"))

        def _parse_api_key_expires_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                api_key_expires_at_type_0 = isoparse(data)

                return api_key_expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        api_key_expires_at = _parse_api_key_expires_at(d.pop("apiKeyExpiresAt", UNSET))

        max_cex_history_days = d.pop("maxCexHistoryDays", UNSET)

        max_cex_import_instruments_per_month = d.pop("maxCexImportInstrumentsPerMonth", UNSET)

        account = cls(
            user_id=user_id,
            tier=tier,
            scopes=scopes,
            max_execute=max_execute,
            max_range_days=max_range_days,
            max_sweep_cartesian=max_sweep_cartesian,
            max_import_range_hours=max_import_range_hours,
            max_cex_import_range_hours=max_cex_import_range_hours,
            max_concurrent_imports=max_concurrent_imports,
            max_datasets=max_datasets,
            max_dataset_bytes=max_dataset_bytes,
            max_total_storage_bytes=max_total_storage_bytes,
            field_links=field_links,
            api_key_expires_at=api_key_expires_at,
            max_cex_history_days=max_cex_history_days,
            max_cex_import_instruments_per_month=max_cex_import_instruments_per_month,
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
