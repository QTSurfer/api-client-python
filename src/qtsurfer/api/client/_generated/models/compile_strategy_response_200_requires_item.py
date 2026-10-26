from enum import Enum


class CompileStrategyResponse200RequiresItem(str, Enum):
    INDICATORS_PRO = "indicators.pro"

    def __str__(self) -> str:
        return str(self.value)
