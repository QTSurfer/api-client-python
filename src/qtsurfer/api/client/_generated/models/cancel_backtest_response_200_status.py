from enum import Enum


class CancelBacktestResponse200Status(str, Enum):
    CANCELLING = "cancelling"

    def __str__(self) -> str:
        return str(self.value)
