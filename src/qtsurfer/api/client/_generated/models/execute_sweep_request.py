from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.equity_curve_request import EquityCurveRequest
    from ..models.sweep_base_config import SweepBaseConfig
    from ..models.sweep_spec_request import SweepSpecRequest
    from ..models.walk_forward_request import WalkForwardRequest


T = TypeVar("T", bound="ExecuteSweepRequest")


@_attrs_define
class ExecuteSweepRequest:
    """
    Attributes:
        strategy_id (str): Unique identifier for a compiled strategy, derived from the source itself: the same code
            always yields the same id, for every caller. How much formatting the id ignores depends on
            the language — see `POST /strategy` for exactly which rewrites preserve it and which do
            not.
             Example: 6bsh31ikwkuivhtgcoa6s4.
        sweep (SweepSpecRequest):  Example: {'sampler': 'lhs', 'seed': 487221, 'samples': 100, 'objective': 'sharpe',
            'params': {'rsiPeriod': {'from': 7, 'to': 28, 'step': 1}, 'useTrendFilter': {'values': [True, False]}}}.
        base_config (SweepBaseConfig | Unset):
        store_signals (bool | Unset): Store signals for every trial. Keep false for normal sweeps. Default: False.
        shards (int | Unset): Requested horizontal shard count; 0 or omitted selects automatically. Default: 0.
        min_trade_floor (int | Unset): Trials below this trade count are flagged but remain in the results. Default: 30.
        walk_forward (WalkForwardRequest | Unset): Opt in to walk-forward validation. Present, the sweep runs as F
            sequential folds and the result gains a `walkForward` section; absent, nothing about the sweep changes. Two
            requests that differ only in this block are two different sweeps and do not deduplicate against each other.
        equity_curve (EquityCurveRequest | Unset): Selection (`mode`/`n`/`maxPct`) plus the transform preference
            (`resample`/`differential`/`outMode`) applied by `GET .../equityCurve` whenever ITS OWN query params are absent,
            for a curve this sweep retained. The transform half never affects retention or `sweepId` — a caller can always
            override it per-request at read time regardless of what was submitted here.
    """

    strategy_id: str
    sweep: SweepSpecRequest
    base_config: SweepBaseConfig | Unset = UNSET
    store_signals: bool | Unset = False
    shards: int | Unset = 0
    min_trade_floor: int | Unset = 30
    walk_forward: WalkForwardRequest | Unset = UNSET
    equity_curve: EquityCurveRequest | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        strategy_id = self.strategy_id

        sweep = self.sweep.to_dict()

        base_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.base_config, Unset):
            base_config = self.base_config.to_dict()

        store_signals = self.store_signals

        shards = self.shards

        min_trade_floor = self.min_trade_floor

        walk_forward: dict[str, Any] | Unset = UNSET
        if not isinstance(self.walk_forward, Unset):
            walk_forward = self.walk_forward.to_dict()

        equity_curve: dict[str, Any] | Unset = UNSET
        if not isinstance(self.equity_curve, Unset):
            equity_curve = self.equity_curve.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "strategyId": strategy_id,
                "sweep": sweep,
            }
        )
        if base_config is not UNSET:
            field_dict["baseConfig"] = base_config
        if store_signals is not UNSET:
            field_dict["storeSignals"] = store_signals
        if shards is not UNSET:
            field_dict["shards"] = shards
        if min_trade_floor is not UNSET:
            field_dict["minTradeFloor"] = min_trade_floor
        if walk_forward is not UNSET:
            field_dict["walkForward"] = walk_forward
        if equity_curve is not UNSET:
            field_dict["equityCurve"] = equity_curve

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.equity_curve_request import EquityCurveRequest
        from ..models.sweep_base_config import SweepBaseConfig
        from ..models.sweep_spec_request import SweepSpecRequest
        from ..models.walk_forward_request import WalkForwardRequest

        d = dict(src_dict)
        strategy_id = d.pop("strategyId")

        sweep = SweepSpecRequest.from_dict(d.pop("sweep"))

        _base_config = d.pop("baseConfig", UNSET)
        base_config: SweepBaseConfig | Unset
        if isinstance(_base_config, Unset):
            base_config = UNSET
        else:
            base_config = SweepBaseConfig.from_dict(_base_config)

        store_signals = d.pop("storeSignals", UNSET)

        shards = d.pop("shards", UNSET)

        min_trade_floor = d.pop("minTradeFloor", UNSET)

        _walk_forward = d.pop("walkForward", UNSET)
        walk_forward: WalkForwardRequest | Unset
        if isinstance(_walk_forward, Unset):
            walk_forward = UNSET
        else:
            walk_forward = WalkForwardRequest.from_dict(_walk_forward)

        _equity_curve = d.pop("equityCurve", UNSET)
        equity_curve: EquityCurveRequest | Unset
        if isinstance(_equity_curve, Unset):
            equity_curve = UNSET
        else:
            equity_curve = EquityCurveRequest.from_dict(_equity_curve)

        execute_sweep_request = cls(
            strategy_id=strategy_id,
            sweep=sweep,
            base_config=base_config,
            store_signals=store_signals,
            shards=shards,
            min_trade_floor=min_trade_floor,
            walk_forward=walk_forward,
            equity_curve=equity_curve,
        )

        execute_sweep_request.additional_properties = d
        return execute_sweep_request

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
