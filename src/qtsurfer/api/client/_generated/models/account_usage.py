from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_usage_links import AccountUsageLinks
    from ..models.cex_import_instrument_usage import CexImportInstrumentUsage


T = TypeVar("T", bound="AccountUsage")


@_attrs_define
class AccountUsage:
    """Your live usage of the shared storage pool `GET /account`'s `maxTotalStorageBytes` caps.
    Not guaranteed real-time — a just-completed upload or strategy execution may take a short
    moment to be reflected here.

        Attributes:
            datasets_used (int): Active datasets counted — the same set `GET /account`'s `maxDatasets` limits. Example: 2.
            dataset_bytes_used (int): Combined bytes of every active dataset's current version. Example: 15728640.
            signals_used (int): Recorded strategy-execution signal uploads. Example: 1.
            signal_bytes_used (int): Combined bytes of every recorded signal upload. Example: 524288.
            strategies_used (int): Registered strategies (see `GET /strategies`). Example: 4.
            strategy_bytes_used (int): Combined bytes of each registered strategy's source plus its latest compiled
                bytecode. Superseded (non-latest) compilations aren't counted.
                 Example: 40960.
            storage_bytes_used (int): `datasetBytesUsed + signalBytesUsed + strategyBytesUsed` — the number checked
                against `GET /account`'s `maxTotalStorageBytes`.
                 Example: 16293888.
            field_links (AccountUsageLinks): HAL `_links` for `GET /account/usage`
            cex_import_month (str | Unset): The calendar month (UTC, `YYYY-MM`) `cexImportInstruments` counts. Absent on a
                platform that has not adopted the monthly limit. Example: 2026-11.
            cex_import_instruments (list[CexImportInstrumentUsage] | Unset): The instruments of an exchange's history you
                have imported this month, counted per market against `GET /account`'s `maxCexImportInstrumentsPerMonth`. A
                market with none is not listed.
    """

    datasets_used: int
    dataset_bytes_used: int
    signals_used: int
    signal_bytes_used: int
    strategies_used: int
    strategy_bytes_used: int
    storage_bytes_used: int
    field_links: AccountUsageLinks
    cex_import_month: str | Unset = UNSET
    cex_import_instruments: list[CexImportInstrumentUsage] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        datasets_used = self.datasets_used

        dataset_bytes_used = self.dataset_bytes_used

        signals_used = self.signals_used

        signal_bytes_used = self.signal_bytes_used

        strategies_used = self.strategies_used

        strategy_bytes_used = self.strategy_bytes_used

        storage_bytes_used = self.storage_bytes_used

        field_links = self.field_links.to_dict()

        cex_import_month = self.cex_import_month

        cex_import_instruments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.cex_import_instruments, Unset):
            cex_import_instruments = []
            for cex_import_instruments_item_data in self.cex_import_instruments:
                cex_import_instruments_item = cex_import_instruments_item_data.to_dict()
                cex_import_instruments.append(cex_import_instruments_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "datasetsUsed": datasets_used,
                "datasetBytesUsed": dataset_bytes_used,
                "signalsUsed": signals_used,
                "signalBytesUsed": signal_bytes_used,
                "strategiesUsed": strategies_used,
                "strategyBytesUsed": strategy_bytes_used,
                "storageBytesUsed": storage_bytes_used,
                "_links": field_links,
            }
        )
        if cex_import_month is not UNSET:
            field_dict["cexImportMonth"] = cex_import_month
        if cex_import_instruments is not UNSET:
            field_dict["cexImportInstruments"] = cex_import_instruments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_usage_links import AccountUsageLinks
        from ..models.cex_import_instrument_usage import CexImportInstrumentUsage

        d = dict(src_dict)
        datasets_used = d.pop("datasetsUsed")

        dataset_bytes_used = d.pop("datasetBytesUsed")

        signals_used = d.pop("signalsUsed")

        signal_bytes_used = d.pop("signalBytesUsed")

        strategies_used = d.pop("strategiesUsed")

        strategy_bytes_used = d.pop("strategyBytesUsed")

        storage_bytes_used = d.pop("storageBytesUsed")

        field_links = AccountUsageLinks.from_dict(d.pop("_links"))

        cex_import_month = d.pop("cexImportMonth", UNSET)

        _cex_import_instruments = d.pop("cexImportInstruments", UNSET)
        cex_import_instruments: list[CexImportInstrumentUsage] | Unset = UNSET
        if _cex_import_instruments is not UNSET:
            cex_import_instruments = []
            for cex_import_instruments_item_data in _cex_import_instruments:
                cex_import_instruments_item = CexImportInstrumentUsage.from_dict(cex_import_instruments_item_data)

                cex_import_instruments.append(cex_import_instruments_item)

        account_usage = cls(
            datasets_used=datasets_used,
            dataset_bytes_used=dataset_bytes_used,
            signals_used=signals_used,
            signal_bytes_used=signal_bytes_used,
            strategies_used=strategies_used,
            strategy_bytes_used=strategy_bytes_used,
            storage_bytes_used=storage_bytes_used,
            field_links=field_links,
            cex_import_month=cex_import_month,
            cex_import_instruments=cex_import_instruments,
        )

        account_usage.additional_properties = d
        return account_usage

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
