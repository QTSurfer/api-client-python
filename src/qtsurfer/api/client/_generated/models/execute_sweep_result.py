from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.execute_sweep_result_objective import ExecuteSweepResultObjective
from ..models.execute_sweep_result_order import ExecuteSweepResultOrder
from ..models.execute_sweep_result_ranking import ExecuteSweepResultRanking
from ..models.execute_sweep_result_status import ExecuteSweepResultStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sweep_progress import SweepProgress
    from ..models.sweep_run_row import SweepRunRow
    from ..models.walk_forward_result import WalkForwardResult


T = TypeVar("T", bound="ExecuteSweepResult")


@_attrs_define
class ExecuteSweepResult:
    """
    Attributes:
        sweep_id (str):
        status (ExecuteSweepResultStatus):
        objective (ExecuteSweepResultObjective):
        order (ExecuteSweepResultOrder):
        progress (SweepProgress): How far along a sweep is, and — when the sweep is still running — enough to tell a
            healthy one from a stuck one. The counts partition the shards (or, for a walk-forward sweep, the folds): every
            unit is either finished, failed, waiting to be retried, or not yet started.
        leaderboard_size (int): Total result rows currently available.
        truncated (bool): True only when the ranked view exceeds its display limit.
        leaderboard (list[SweepRunRow]):
        ranking (ExecuteSweepResultRanking | Unset): Which ordering was actually applied, which is not always the one
            requested: a sweep with no stored parameter grid cannot be plateau-ranked and falls back to `raw`. Always `raw`
            when `order=natural`.
        pbo (float | Unset): Probability of backtest overfitting for the sweep as a whole, by combinatorially symmetric
            cross-validation: how often the configuration that won in-sample lands below median out-of-sample. Above ~0.5
            the sweep is selecting noise, whatever its top row says. Computed once when the last shard finishes, so it is
            absent while the sweep is still running and on sweeps too small for the statistic to mean anything.
        pbo_splits (int | Unset): How many train/test splits the `pbo` figure was averaged over.
        walk_forward (WalkForwardResult | Unset): Present only on a sweep submitted with `walkForward`, and present from
            acceptance onward — its presence, not its contents, is what identifies a walk-forward sweep. `completedFolds` is
            0 while the first fold is still running.
    """

    sweep_id: str
    status: ExecuteSweepResultStatus
    objective: ExecuteSweepResultObjective
    order: ExecuteSweepResultOrder
    progress: SweepProgress
    leaderboard_size: int
    truncated: bool
    leaderboard: list[SweepRunRow]
    ranking: ExecuteSweepResultRanking | Unset = UNSET
    pbo: float | Unset = UNSET
    pbo_splits: int | Unset = UNSET
    walk_forward: WalkForwardResult | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sweep_id = self.sweep_id

        status = self.status.value

        objective = self.objective.value

        order = self.order.value

        progress = self.progress.to_dict()

        leaderboard_size = self.leaderboard_size

        truncated = self.truncated

        leaderboard = []
        for leaderboard_item_data in self.leaderboard:
            leaderboard_item = leaderboard_item_data.to_dict()
            leaderboard.append(leaderboard_item)

        ranking: str | Unset = UNSET
        if not isinstance(self.ranking, Unset):
            ranking = self.ranking.value

        pbo = self.pbo

        pbo_splits = self.pbo_splits

        walk_forward: dict[str, Any] | Unset = UNSET
        if not isinstance(self.walk_forward, Unset):
            walk_forward = self.walk_forward.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sweepId": sweep_id,
                "status": status,
                "objective": objective,
                "order": order,
                "progress": progress,
                "leaderboardSize": leaderboard_size,
                "truncated": truncated,
                "leaderboard": leaderboard,
            }
        )
        if ranking is not UNSET:
            field_dict["ranking"] = ranking
        if pbo is not UNSET:
            field_dict["pbo"] = pbo
        if pbo_splits is not UNSET:
            field_dict["pboSplits"] = pbo_splits
        if walk_forward is not UNSET:
            field_dict["walkForward"] = walk_forward

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sweep_progress import SweepProgress
        from ..models.sweep_run_row import SweepRunRow
        from ..models.walk_forward_result import WalkForwardResult

        d = dict(src_dict)
        sweep_id = d.pop("sweepId")

        status = ExecuteSweepResultStatus(d.pop("status"))

        objective = ExecuteSweepResultObjective(d.pop("objective"))

        order = ExecuteSweepResultOrder(d.pop("order"))

        progress = SweepProgress.from_dict(d.pop("progress"))

        leaderboard_size = d.pop("leaderboardSize")

        truncated = d.pop("truncated")

        leaderboard = []
        _leaderboard = d.pop("leaderboard")
        for leaderboard_item_data in _leaderboard:
            leaderboard_item = SweepRunRow.from_dict(leaderboard_item_data)

            leaderboard.append(leaderboard_item)

        _ranking = d.pop("ranking", UNSET)
        ranking: ExecuteSweepResultRanking | Unset
        if isinstance(_ranking, Unset):
            ranking = UNSET
        else:
            ranking = ExecuteSweepResultRanking(_ranking)

        pbo = d.pop("pbo", UNSET)

        pbo_splits = d.pop("pboSplits", UNSET)

        _walk_forward = d.pop("walkForward", UNSET)
        walk_forward: WalkForwardResult | Unset
        if isinstance(_walk_forward, Unset):
            walk_forward = UNSET
        else:
            walk_forward = WalkForwardResult.from_dict(_walk_forward)

        execute_sweep_result = cls(
            sweep_id=sweep_id,
            status=status,
            objective=objective,
            order=order,
            progress=progress,
            leaderboard_size=leaderboard_size,
            truncated=truncated,
            leaderboard=leaderboard,
            ranking=ranking,
            pbo=pbo,
            pbo_splits=pbo_splits,
            walk_forward=walk_forward,
        )

        execute_sweep_result.additional_properties = d
        return execute_sweep_result

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
