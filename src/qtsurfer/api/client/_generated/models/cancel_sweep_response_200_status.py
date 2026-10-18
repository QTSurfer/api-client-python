from enum import Enum


class CancelSweepResponse200Status(str, Enum):
    CANCELLING = "cancelling"

    def __str__(self) -> str:
        return str(self.value)
