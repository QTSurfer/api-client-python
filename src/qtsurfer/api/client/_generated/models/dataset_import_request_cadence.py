from enum import Enum


class DatasetImportRequestCadence(str, Enum):
    VALUE_0 = "1s"
    VALUE_1 = "1m"
    VALUE_2 = "5m"

    def __str__(self) -> str:
        return str(self.value)
