from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DatasetImportRequestMeta")


@_attrs_define
class DatasetImportRequestMeta:
    """Optional. Keys of your own to keep on the dataset, returned as `meta` of the `Dataset`
    beside the ones the import records itself. Two namespaces are yours: `pool.*`, a note
    about the pool the import is for (by convention `pool.id`, `pool.name`, `pool.dex`,
    `pool.reserve_usd`, `pool.created_at`), and `user.*`, any label you like. A key of the
    platform's (`import.*`, `dex.*`, `cex.*`) or of any other namespace is `400`.

    A key is lower-case letters, digits and `_`, in parts separated by `.`, at most 64
    characters. A value is a non-empty text of at most 256 characters with no control
    characters. At most 16 keys, and the whole of what is kept (your keys and the ones the
    import adds) at most 32 keys and 4096 bytes of JSON. Anything over a limit is `400`; the
    import is not created. `meta` is not taken by `POST /datasets`.

        Example:
            {'pool.name': 'FiveM / SOL', 'pool.dex': 'PumpSwap', 'user.label': 'week one'}

    """

    additional_properties: dict[str, str] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dataset_import_request_meta = cls()

        dataset_import_request_meta.additional_properties = d
        return dataset_import_request_meta

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
