from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.equity_curve_options import EquityCurveOptions


T = TypeVar("T", bound="ExecuteBacktestBody")


@_attrs_define
class ExecuteBacktestBody:
    """
    Attributes:
        prepare_job_id (str): Job ID returned by `POST /prepare` (must be in `Completed` state) Example:
            13RBLGQlPnfDjO6wyKSX8i.
        strategy_id (str): Unique identifier for a compiled strategy, derived from the source itself: the same code
            always yields the same id, for every caller, whatever its formatting. See
            `POST /strategy` for exactly which rewrites preserve it and which do not.
             Example: 6bsh31ikwkuivhtgcoa6s4.
        store_signals (bool | Unset): When true, the worker uploads emitted signals to object storage and the
            response includes `signalsUrl` / `signalsId` fields. Defaults to false.
             Default: False.
        equity_curve (EquityCurveOptions | Unset): Requested equity-curve transform, applied server-side in a fixed
            pipeline order: `resample` (point count) then `differential` (encoding) then `outMode` (JSON shape) — each stage
            assumes the previous one already ran. A server-side size guard can still force a smaller/deflated shape above
            its thresholds regardless of what is requested here — see `EquityCurveMeta` for what actually happened.
    """

    prepare_job_id: str
    strategy_id: str
    store_signals: bool | Unset = False
    equity_curve: EquityCurveOptions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        prepare_job_id = self.prepare_job_id

        strategy_id = self.strategy_id

        store_signals = self.store_signals

        equity_curve: dict[str, Any] | Unset = UNSET
        if not isinstance(self.equity_curve, Unset):
            equity_curve = self.equity_curve.to_dict()

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
        if equity_curve is not UNSET:
            field_dict["equityCurve"] = equity_curve

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.equity_curve_options import EquityCurveOptions

        d = dict(src_dict)
        prepare_job_id = d.pop("prepareJobId")

        strategy_id = d.pop("strategyId")

        store_signals = d.pop("storeSignals", UNSET)

        _equity_curve = d.pop("equityCurve", UNSET)
        equity_curve: EquityCurveOptions | Unset
        if isinstance(_equity_curve, Unset):
            equity_curve = UNSET
        else:
            equity_curve = EquityCurveOptions.from_dict(_equity_curve)

        execute_backtest_body = cls(
            prepare_job_id=prepare_job_id,
            strategy_id=strategy_id,
            store_signals=store_signals,
            equity_curve=equity_curve,
        )

        execute_backtest_body.additional_properties = d
        return execute_backtest_body

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
