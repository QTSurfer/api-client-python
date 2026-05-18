from enum import Enum


class DataSourceType(str, Enum):
    TICKER = "ticker"

    def __str__(self) -> str:
        return str(self.value)
