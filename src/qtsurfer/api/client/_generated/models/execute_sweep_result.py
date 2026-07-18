from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.execute_sweep_result_objective import ExecuteSweepResultObjective
from ..models.execute_sweep_result_order import ExecuteSweepResultOrder
from ..models.execute_sweep_result_status import ExecuteSweepResultStatus

if TYPE_CHECKING:
    from ..models.sweep_progress import SweepProgress
    from ..models.sweep_run_row import SweepRunRow


T = TypeVar("T", bound="ExecuteSweepResult")


@_attrs_define
class ExecuteSweepResult:
    """
    Attributes:
        sweep_id (str):
        status (ExecuteSweepResultStatus):
        objective (ExecuteSweepResultObjective):
        order (ExecuteSweepResultOrder):
        progress (SweepProgress):
        leaderboard_size (int): Total result rows currently available.
        truncated (bool): True only when the ranked view exceeds its display limit.
        leaderboard (list[SweepRunRow]):
    """

    sweep_id: str
    status: ExecuteSweepResultStatus
    objective: ExecuteSweepResultObjective
    order: ExecuteSweepResultOrder
    progress: SweepProgress
    leaderboard_size: int
    truncated: bool
    leaderboard: list[SweepRunRow]
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sweep_progress import SweepProgress
        from ..models.sweep_run_row import SweepRunRow

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

        execute_sweep_result = cls(
            sweep_id=sweep_id,
            status=status,
            objective=objective,
            order=order,
            progress=progress,
            leaderboard_size=leaderboard_size,
            truncated=truncated,
            leaderboard=leaderboard,
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
