from enum import Enum


class DatasetCreatedType(str, Enum):
    TICKER = "ticker"

    def __str__(self) -> str:
        return str(self.value)
