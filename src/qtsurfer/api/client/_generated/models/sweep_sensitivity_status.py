from enum import Enum


class SweepSensitivityStatus(str, Enum):
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"
    PARTIAL = "PARTIAL"
    RUNNING = "RUNNING"

    def __str__(self) -> str:
        return str(self.value)
