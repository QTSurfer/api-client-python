from enum import Enum


class PrepareJobStateHoursWithoutDataItemRationale(str, Enum):
    LOW_ACTIVITY = "low_activity"
    PENDING_CONVERSION = "pending_conversion"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
