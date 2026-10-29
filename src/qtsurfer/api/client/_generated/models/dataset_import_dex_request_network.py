from enum import Enum


class DatasetImportDexRequestNetwork(str, Enum):
    ETHEREUM = "ethereum"
    ROBINHOOD = "robinhood"
    SOLANA = "solana"

    def __str__(self) -> str:
        return str(self.value)
