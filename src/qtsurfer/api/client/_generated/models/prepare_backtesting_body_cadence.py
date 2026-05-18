from enum import Enum


class PrepareBacktestingBodyCadence(str, Enum):
    VALUE_0 = "1s"
    VALUE_1 = "5s"
    VALUE_2 = "1m"
    VALUE_3 = "5m"
    VALUE_4 = "15m"
    VALUE_5 = "1h"
    VALUE_6 = "4h"
    VALUE_7 = "1d"

    def __str__(self) -> str:
        return str(self.value)
