from enum import Enum


class StrategyStateRequiredSourcesItem(str, Enum):
    FUNDINGRATE = "FundingRate"
    KLINE = "KLine"
    TICKER = "Ticker"

    def __str__(self) -> str:
        return str(self.value)
