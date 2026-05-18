from enum import Enum


class JobStateStatus(str, Enum):
    ABORTED = "Aborted"
    COMPLETED = "Completed"
    FAILED = "Failed"
    NEW = "New"
    PARTIAL = "Partial"
    STARTED = "Started"

    def __str__(self) -> str:
        return str(self.value)
