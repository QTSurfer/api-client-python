from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_strategy_status_response_200_status import GetStrategyStatusResponse200Status
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetStrategyStatusResponse200")


@_attrs_define
class GetStrategyStatusResponse200:
    """
    Attributes:
        status (GetStrategyStatusResponse200Status):  Example: Completed.
        job_id (str | Unset): Compile job id (only set in async mode) Example: 6bsh31ikwkuivhtgcoa6s4.
        strategy_id (str | Unset): Unique identifier for a compiled strategy Example: 6bsh31ikwkuivhtgcoa6s4.
        status_detail (None | str | Unset): Compilation error messages when `status` is `Failed`
    """

    status: GetStrategyStatusResponse200Status
    job_id: str | Unset = UNSET
    strategy_id: str | Unset = UNSET
    status_detail: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        job_id = self.job_id

        strategy_id = self.strategy_id

        status_detail: None | str | Unset
        if isinstance(self.status_detail, Unset):
            status_detail = UNSET
        else:
            status_detail = self.status_detail

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if job_id is not UNSET:
            field_dict["jobId"] = job_id
        if strategy_id is not UNSET:
            field_dict["strategyId"] = strategy_id
        if status_detail is not UNSET:
            field_dict["statusDetail"] = status_detail

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = GetStrategyStatusResponse200Status(d.pop("status"))

        job_id = d.pop("jobId", UNSET)

        strategy_id = d.pop("strategyId", UNSET)

        def _parse_status_detail(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status_detail = _parse_status_detail(d.pop("statusDetail", UNSET))

        get_strategy_status_response_200 = cls(
            status=status,
            job_id=job_id,
            strategy_id=strategy_id,
            status_detail=status_detail,
        )

        get_strategy_status_response_200.additional_properties = d
        return get_strategy_status_response_200

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
