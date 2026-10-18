from enum import Enum


class LiveRunSummaryStage(str, Enum):
    LIVE = "LIVE"
    SANDBOX = "SANDBOX"

    def __str__(self) -> str:
        return str(self.value)
