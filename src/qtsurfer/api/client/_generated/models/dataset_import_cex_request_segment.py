from enum import Enum


class DatasetImportCexRequestSegment(str, Enum):
    SPOT = "spot"

    def __str__(self) -> str:
        return str(self.value)
