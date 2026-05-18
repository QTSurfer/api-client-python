from enum import Enum


class CancelExecutionResponse200Status(str, Enum):
    CANCELLING = "cancelling"

    def __str__(self) -> str:
        return str(self.value)
