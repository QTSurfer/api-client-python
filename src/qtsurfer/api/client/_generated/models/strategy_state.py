from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.strategy_state_required_sources_item import StrategyStateRequiredSourcesItem
from ..models.strategy_state_validation import StrategyStateValidation
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notice import Notice
    from ..models.strategy_links import StrategyLinks


T = TypeVar("T", bound="StrategyState")


@_attrs_define
class StrategyState:
    """What is known about a registered strategy: that it compiled, and what validating it found.

    **`validation: passed` does not mean the strategy is correct.** It means the class loaded and
    survived the first event of a short synthetic run — a floor, not a guarantee. When
    `dryRunIncomplete` is true it is a lower floor still, because the run did not finish.

        Example:
            {'strategyId': '6bsh31ikwkuivhtgcoa6s4', 'validation': 'passed', 'compiledAt': '2026-08-04T16:23:04Z',
                'requiredSources': ['Ticker'], 'validatedAt': '2026-08-04T16:24:11Z', 'notices': [{'level': 'WARN', 'code':
                'indicator.bar-data-on-ticker-path', 'message': 'Indicator requires bar data but is on the ticker path',
                'provenance': 'compile-dry-run'}], '_links': {'code': {'href': '/v1/strategy/6bsh31ikwkuivhtgcoa6s4/code'}}}

        Attributes:
            strategy_id (str): Unique identifier for a compiled strategy, derived from the source itself: the same code
                always yields the same id, for every caller, whatever its formatting. See
                `POST /strategy` for exactly which rewrites preserve it and which do not.
                 Example: 6bsh31ikwkuivhtgcoa6s4.
            validation (StrategyStateValidation): * `not_validated` — registered, never checked. `POST
                /strategy/{strategyId}/validate`
                  checks it.
                * `pending` — a check was asked for and has not answered yet.
                * `passed` — the class loaded and survived its first event.
                * `failed` — it did not; `detail` says how.
                 Example: passed.
            compiled_at (datetime.datetime | Unset): When the live compilation was produced.
            required_sources (list[StrategyStateRequiredSourcesItem] | Unset): The market data a strategy needs, read off
                the compiled class rather than off anything
                you sent — `TickerStrategy`, `KlineStrategy` and `FundingRateStrategy` each declare one,
                and a `MultiSourceStrategy` declares a set.

                **Absent is not "needs nothing".** A strategy always needs market data, so an absent
                field never means an empty requirement — it means the platform could not establish the
                answer without constructing your strategy, which it will not do to fill in a field.
                That happens for a `MultiSourceStrategy`, for a class that overrides
                `getMarketDataSource()`, and for anything registered before this field existed;
                re-registering the source fills it in.
                 Example: ['Ticker'].
            validated_at (datetime.datetime | Unset): When the verdict was recorded. Absent until there is one.
            detail (str | Unset): Why validation failed, or why a queued check has not reported. Present on `failed`, and
                alongside `validationStalled`.
            notices (list[Notice] | Unset): What the run surfaced. An empty or absent list is not a clean bill of health
                when
                `dryRunIncomplete` is true — see that field.
            notices_truncated (int | Unset): How many notices were dropped past the cap. Absent when none were. Example: 3.
            dry_run_incomplete (bool | Unset): The check did not finish its budget — it ran out of time, was refused because
                the
                platform was already holding too many unfinishable runs, or hit a failure attributable to
                the synthetic instrument rather than to your strategy. The verdict stands as far as it
                went; it simply reached less than a full run would.
            validation_stalled (bool | Unset): A queued check has not reported for far longer than one takes. Nothing is
                disproved about
                the strategy — the check has not run. Stop waiting and re-request it later.
            field_links (StrategyLinks | Unset): HAL `_links` for a strategy — present on a full `StrategyState` body (`GET
                /strategy/{strategyId}`, and `POST /strategy/{strategyId}/validate`'s already-validated
                `200`), absent from that same endpoint's `202` — a deliberately partial stub carrying only
                what is known before a check has even started. Following `code` can still `404` once
                present: it documents its own honest "nothing to return" for a strategy with no source of
                its own (a `REFERENCE` marketplace copy, or one resolved only through the platform's shared
                pool). This link says where to look, not that something is there.
    """

    strategy_id: str
    validation: StrategyStateValidation
    compiled_at: datetime.datetime | Unset = UNSET
    required_sources: list[StrategyStateRequiredSourcesItem] | Unset = UNSET
    validated_at: datetime.datetime | Unset = UNSET
    detail: str | Unset = UNSET
    notices: list[Notice] | Unset = UNSET
    notices_truncated: int | Unset = UNSET
    dry_run_incomplete: bool | Unset = UNSET
    validation_stalled: bool | Unset = UNSET
    field_links: StrategyLinks | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        strategy_id = self.strategy_id

        validation = self.validation.value

        compiled_at: str | Unset = UNSET
        if not isinstance(self.compiled_at, Unset):
            compiled_at = self.compiled_at.isoformat()

        required_sources: list[str] | Unset = UNSET
        if not isinstance(self.required_sources, Unset):
            required_sources = []
            for required_sources_item_data in self.required_sources:
                required_sources_item = required_sources_item_data.value
                required_sources.append(required_sources_item)

        validated_at: str | Unset = UNSET
        if not isinstance(self.validated_at, Unset):
            validated_at = self.validated_at.isoformat()

        detail = self.detail

        notices: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.notices, Unset):
            notices = []
            for notices_item_data in self.notices:
                notices_item = notices_item_data.to_dict()
                notices.append(notices_item)

        notices_truncated = self.notices_truncated

        dry_run_incomplete = self.dry_run_incomplete

        validation_stalled = self.validation_stalled

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "strategyId": strategy_id,
                "validation": validation,
            }
        )
        if compiled_at is not UNSET:
            field_dict["compiledAt"] = compiled_at
        if required_sources is not UNSET:
            field_dict["requiredSources"] = required_sources
        if validated_at is not UNSET:
            field_dict["validatedAt"] = validated_at
        if detail is not UNSET:
            field_dict["detail"] = detail
        if notices is not UNSET:
            field_dict["notices"] = notices
        if notices_truncated is not UNSET:
            field_dict["noticesTruncated"] = notices_truncated
        if dry_run_incomplete is not UNSET:
            field_dict["dryRunIncomplete"] = dry_run_incomplete
        if validation_stalled is not UNSET:
            field_dict["validationStalled"] = validation_stalled
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notice import Notice
        from ..models.strategy_links import StrategyLinks

        d = dict(src_dict)
        strategy_id = d.pop("strategyId")

        validation = StrategyStateValidation(d.pop("validation"))

        _compiled_at = d.pop("compiledAt", UNSET)
        compiled_at: datetime.datetime | Unset
        if isinstance(_compiled_at, Unset):
            compiled_at = UNSET
        else:
            compiled_at = isoparse(_compiled_at)

        _required_sources = d.pop("requiredSources", UNSET)
        required_sources: list[StrategyStateRequiredSourcesItem] | Unset = UNSET
        if _required_sources is not UNSET:
            required_sources = []
            for required_sources_item_data in _required_sources:
                required_sources_item = StrategyStateRequiredSourcesItem(required_sources_item_data)

                required_sources.append(required_sources_item)

        _validated_at = d.pop("validatedAt", UNSET)
        validated_at: datetime.datetime | Unset
        if isinstance(_validated_at, Unset):
            validated_at = UNSET
        else:
            validated_at = isoparse(_validated_at)

        detail = d.pop("detail", UNSET)

        _notices = d.pop("notices", UNSET)
        notices: list[Notice] | Unset = UNSET
        if _notices is not UNSET:
            notices = []
            for notices_item_data in _notices:
                notices_item = Notice.from_dict(notices_item_data)

                notices.append(notices_item)

        notices_truncated = d.pop("noticesTruncated", UNSET)

        dry_run_incomplete = d.pop("dryRunIncomplete", UNSET)

        validation_stalled = d.pop("validationStalled", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: StrategyLinks | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = StrategyLinks.from_dict(_field_links)

        strategy_state = cls(
            strategy_id=strategy_id,
            validation=validation,
            compiled_at=compiled_at,
            required_sources=required_sources,
            validated_at=validated_at,
            detail=detail,
            notices=notices,
            notices_truncated=notices_truncated,
            dry_run_incomplete=dry_run_incomplete,
            validation_stalled=validation_stalled,
            field_links=field_links,
        )

        strategy_state.additional_properties = d
        return strategy_state

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
