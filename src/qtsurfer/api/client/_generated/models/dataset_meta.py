from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DatasetMeta")


@_attrs_define
class DatasetMeta:
    """How the dataset came to be: a flat map of text to text, written once when the dataset
    is created and never changed afterwards. Always present, `{}` when nothing was recorded
    (an upload, or a dataset created before this field existed). It is information for
    whoever looks at the dataset, not something the API decides anything from.

    An import records what it was asked for, under keys that begin with `import.`
    (`import.type`, `import.cadence`, `import.from`, `import.to`, the range requested),
    `dex.` (`dex.network`, `dex.contract`, `dex.id`, `dex.version`, `dex.factory`) or `cex.`
    (`cex.exchange`, `cex.segment`, `cex.data_type`). A key with no value is left out. The
    keys the caller sent with the import (`pool.*`, `user.*`, see `DatasetImportRequest`)
    come back beside them.

        Example:
            {'import.type': 'dex', 'import.cadence': '1s', 'import.from': '2026-11-16T00:25:02Z', 'import.to':
                '2026-11-16T10:30:00Z', 'dex.network': 'solana', 'dex.contract': '6nwmQSgHWtRfXw9xqQM3hseyKzWrQq2gzamoSbjKqs32',
                'pool.name': 'FiveM / SOL'}

    """

    additional_properties: dict[str, str] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dataset_meta = cls()

        dataset_meta.additional_properties = d
        return dataset_meta

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> str:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: str) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
