from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.live_paper_stage import LivePaperStage

if TYPE_CHECKING:
    from ..models.live_paper_account import LivePaperAccount


T = TypeVar("T", bound="LivePaper")


@_attrs_define
class LivePaper:
    """
    Attributes:
        run_id (str):
        stage (LivePaperStage):
        accounts (list[LivePaperAccount]):
    """

    run_id: str
    stage: LivePaperStage
    accounts: list[LivePaperAccount]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        run_id = self.run_id

        stage = self.stage.value

        accounts = []
        for accounts_item_data in self.accounts:
            accounts_item = accounts_item_data.to_dict()
            accounts.append(accounts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "runId": run_id,
                "stage": stage,
                "accounts": accounts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.live_paper_account import LivePaperAccount

        d = dict(src_dict)
        run_id = d.pop("runId")

        stage = LivePaperStage(d.pop("stage"))

        accounts = []
        _accounts = d.pop("accounts")
        for accounts_item_data in _accounts:
            accounts_item = LivePaperAccount.from_dict(accounts_item_data)

            accounts.append(accounts_item)

        live_paper = cls(
            run_id=run_id,
            stage=stage,
            accounts=accounts,
        )

        live_paper.additional_properties = d
        return live_paper

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
