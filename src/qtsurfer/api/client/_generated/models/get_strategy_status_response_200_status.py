from enum import Enum


class GetStrategyStatusResponse200Status(str, Enum):
    ABORTED = "Aborted"
    COMPLETED = "Completed"
    FAILED = "Failed"
    NEW = "New"
    STARTED = "Started"

    def __str__(self) -> str:
        return str(self.value)
