from enum import Enum


class PrepareRequestCadence(str, Enum):
    VALUE_0 = "1s"
    VALUE_1 = "5s"
    VALUE_10 = "8h"
    VALUE_11 = "12h"
    VALUE_12 = "1d"
    VALUE_13 = "1w"
    VALUE_14 = "1q"
    VALUE_2 = "1m"
    VALUE_3 = "3m"
    VALUE_4 = "5m"
    VALUE_5 = "15m"
    VALUE_6 = "30m"
    VALUE_7 = "1h"
    VALUE_8 = "2h"
    VALUE_9 = "4h"

    def __str__(self) -> str:
        return str(self.value)
