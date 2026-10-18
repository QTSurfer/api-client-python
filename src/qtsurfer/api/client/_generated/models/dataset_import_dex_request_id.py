from enum import Enum


class DatasetImportDexRequestId(str, Enum):
    UNISWAP = "uniswap"

    def __str__(self) -> str:
        return str(self.value)
