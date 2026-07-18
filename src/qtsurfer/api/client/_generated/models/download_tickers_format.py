from enum import Enum


class DownloadTickersFormat(str, Enum):
    LASTRA = "lastra"
    PARQUET = "parquet"

    def __str__(self) -> str:
        return str(self.value)
