from enum import Enum


class DatasetImportDexRequestVersion(str, Enum):
    V2 = "v2"
    V3 = "v3"

    def __str__(self) -> str:
        return str(self.value)
