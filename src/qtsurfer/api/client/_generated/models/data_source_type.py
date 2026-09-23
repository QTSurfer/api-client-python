from enum import Enum


class DataSourceType(str, Enum):
    FUNDING = "funding"
    KLINE = "kline"
    TICKER = "ticker"

    def __str__(self) -> str:
        return str(self.value)
