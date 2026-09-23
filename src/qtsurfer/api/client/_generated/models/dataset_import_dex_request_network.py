from enum import Enum


class DatasetImportDexRequestNetwork(str, Enum):
    ETHEREUM = "ethereum"
    ROBINHOOD = "robinhood"

    def __str__(self) -> str:
        return str(self.value)
