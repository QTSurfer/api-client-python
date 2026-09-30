from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sweep_spec_request_objective import SweepSpecRequestObjective
from ..models.sweep_spec_request_sampler import SweepSpecRequestSampler
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sweep_spec_request_params import SweepSpecRequestParams


T = TypeVar("T", bound="SweepSpecRequest")


@_attrs_define
class SweepSpecRequest:
    """
    Example:
        {'sampler': 'lhs', 'seed': 487221, 'samples': 100, 'objective': 'sharpe', 'params': {'rsiPeriod': {'from': 7,
            'to': 28, 'step': 1}, 'useTrendFilter': {'values': [True, False]}}}

    Attributes:
        params (SweepSpecRequestParams):
        sampler (SweepSpecRequestSampler | Unset): `grid` runs every combination of the axes and is held to your plan's
            `maxSweepCartesian` (`GET /account`); `random` and `lhs` run `samples` combinations and are not.
             Default: SweepSpecRequestSampler.GRID.
        seed (int | Unset): Reproducibility seed. If omitted, the server generates one with Java's
            `L64X128MixRandom` generator and returns the effective value. The range
            is limited to JavaScript-safe integers so generated clients can replay it exactly.
        samples (int | Unset): Number of samples for `random` and `lhs`; ignored by `grid`.
        objective (SweepSpecRequestObjective | Unset):  Default: SweepSpecRequestObjective.SHARPE.
    """

    params: SweepSpecRequestParams
    sampler: SweepSpecRequestSampler | Unset = SweepSpecRequestSampler.GRID
    seed: int | Unset = UNSET
    samples: int | Unset = UNSET
    objective: SweepSpecRequestObjective | Unset = SweepSpecRequestObjective.SHARPE
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        params = self.params.to_dict()

        sampler: str | Unset = UNSET
        if not isinstance(self.sampler, Unset):
            sampler = self.sampler.value

        seed = self.seed

        samples = self.samples

        objective: str | Unset = UNSET
        if not isinstance(self.objective, Unset):
            objective = self.objective.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "params": params,
            }
        )
        if sampler is not UNSET:
            field_dict["sampler"] = sampler
        if seed is not UNSET:
            field_dict["seed"] = seed
        if samples is not UNSET:
            field_dict["samples"] = samples
        if objective is not UNSET:
            field_dict["objective"] = objective

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sweep_spec_request_params import SweepSpecRequestParams

        d = dict(src_dict)
        params = SweepSpecRequestParams.from_dict(d.pop("params"))

        _sampler = d.pop("sampler", UNSET)
        sampler: SweepSpecRequestSampler | Unset
        if isinstance(_sampler, Unset):
            sampler = UNSET
        else:
            sampler = SweepSpecRequestSampler(_sampler)

        seed = d.pop("seed", UNSET)

        samples = d.pop("samples", UNSET)

        _objective = d.pop("objective", UNSET)
        objective: SweepSpecRequestObjective | Unset
        if isinstance(_objective, Unset):
            objective = UNSET
        else:
            objective = SweepSpecRequestObjective(_objective)

        sweep_spec_request = cls(
            params=params,
            sampler=sampler,
            seed=seed,
            samples=samples,
            objective=objective,
        )

        sweep_spec_request.additional_properties = d
        return sweep_spec_request

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
