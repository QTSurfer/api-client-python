from enum import Enum


class DatasetImportStateStatus(str, Enum):
    FAILED = "failed"
    FETCHING = "fetching"
    INGESTING = "ingesting"
    READY = "ready"

    def __str__(self) -> str:
        return str(self.value)
