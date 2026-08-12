from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.sweep_run_row import SweepRunRow
    from ..models.walk_forward_fold_params import WalkForwardFoldParams


T = TypeVar("T", bound="WalkForwardFold")


@_attrs_define
class WalkForwardFold:
    """What one fold concluded. The out-of-sample row is the answer; the in-sample figure is only there to be compared
    against it, since any grid produces a flattering in-sample winner — that is what optimizing does. The gap between
    them is the whole reading.

        Attributes:
            fold_ix (int): Position in the walk-forward sequence, oldest first.
            in_sample_from (int): First index of the optimization window, into the prepared session.
            in_sample_to (int): End of the optimization window, exclusive — and where scoring begins.
            out_of_sample_to (int): End of the scoring window, exclusive.
            params (WalkForwardFoldParams): The parameter vector that won this fold's optimization window.
            in_sample_sharpe (float): How that winner scored on the window it was chosen on.
            out_of_sample (SweepRunRow):
            vectors_run (int): Vectors this fold evaluated in-sample before picking its winner.
    """

    fold_ix: int
    in_sample_from: int
    in_sample_to: int
    out_of_sample_to: int
    params: WalkForwardFoldParams
    in_sample_sharpe: float
    out_of_sample: SweepRunRow
    vectors_run: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fold_ix = self.fold_ix

        in_sample_from = self.in_sample_from

        in_sample_to = self.in_sample_to

        out_of_sample_to = self.out_of_sample_to

        params = self.params.to_dict()

        in_sample_sharpe = self.in_sample_sharpe

        out_of_sample = self.out_of_sample.to_dict()

        vectors_run = self.vectors_run

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "foldIx": fold_ix,
                "inSampleFrom": in_sample_from,
                "inSampleTo": in_sample_to,
                "outOfSampleTo": out_of_sample_to,
                "params": params,
                "inSampleSharpe": in_sample_sharpe,
                "outOfSample": out_of_sample,
                "vectorsRun": vectors_run,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sweep_run_row import SweepRunRow
        from ..models.walk_forward_fold_params import WalkForwardFoldParams

        d = dict(src_dict)
        fold_ix = d.pop("foldIx")

        in_sample_from = d.pop("inSampleFrom")

        in_sample_to = d.pop("inSampleTo")

        out_of_sample_to = d.pop("outOfSampleTo")

        params = WalkForwardFoldParams.from_dict(d.pop("params"))

        in_sample_sharpe = d.pop("inSampleSharpe")

        out_of_sample = SweepRunRow.from_dict(d.pop("outOfSample"))

        vectors_run = d.pop("vectorsRun")

        walk_forward_fold = cls(
            fold_ix=fold_ix,
            in_sample_from=in_sample_from,
            in_sample_to=in_sample_to,
            out_of_sample_to=out_of_sample_to,
            params=params,
            in_sample_sharpe=in_sample_sharpe,
            out_of_sample=out_of_sample,
            vectors_run=vectors_run,
        )

        walk_forward_fold.additional_properties = d
        return walk_forward_fold

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
