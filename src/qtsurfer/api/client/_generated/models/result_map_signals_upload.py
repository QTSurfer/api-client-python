from enum import Enum


class ResultMapSignalsUpload(str, Enum):
    DONE = "Done"
    FAILED = "Failed"
    SKIPPED = "Skipped"

    def __str__(self) -> str:
        return str(self.value)
