from enum import Enum


class DatasetUploadStateStatus(str, Enum):
    FAILED = "failed"
    INGESTING = "ingesting"
    READY = "ready"
    UPLOADING = "uploading"

    def __str__(self) -> str:
        return str(self.value)
