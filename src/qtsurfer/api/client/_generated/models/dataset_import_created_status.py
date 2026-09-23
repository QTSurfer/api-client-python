from enum import Enum


class DatasetImportCreatedStatus(str, Enum):
    FETCHING = "fetching"

    def __str__(self) -> str:
        return str(self.value)
