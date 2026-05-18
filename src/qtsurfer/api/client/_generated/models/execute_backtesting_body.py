from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExecuteBacktestingBody")


@_attrs_define
class ExecuteBacktestingBody:
    """
    Attributes:
        prepare_job_id (str): Job ID returned by `POST /prepare` (must be in `Completed` state) Example:
            13RBLGQlPnfDjO6wyKSX8i.
        strategy_id (str): Unique identifier for a compiled strategy Example: 6bsh31ikwkuivhtgcoa6s4.
        store_signals (bool | Unset): When true, the worker uploads emitted signals to object storage and the
            response includes `signalsUrl` / `signalsId` fields. Defaults to false.
             Default: False.
    """

    prepare_job_id: str
    strategy_id: str
    store_signals: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        prepare_job_id = self.prepare_job_id

        strategy_id = self.strategy_id

        store_signals = self.store_signals

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "prepareJobId": prepare_job_id,
                "strategyId": strategy_id,
            }
        )
        if store_signals is not UNSET:
            field_dict["storeSignals"] = store_signals

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        prepare_job_id = d.pop("prepareJobId")

        strategy_id = d.pop("strategyId")

        store_signals = d.pop("storeSignals", UNSET)

        execute_backtesting_body = cls(
            prepare_job_id=prepare_job_id,
            strategy_id=strategy_id,
            store_signals=store_signals,
        )

        execute_backtesting_body.additional_properties = d
        return execute_backtesting_body

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
