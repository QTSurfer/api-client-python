from enum import Enum


class DatasetImportCexRequestDataType(str, Enum):
    KLINES = "klines"
    TICKER = "ticker"

    def __str__(self) -> str:
        return str(self.value)
