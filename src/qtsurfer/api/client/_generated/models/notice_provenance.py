from enum import Enum


class NoticeProvenance(str, Enum):
    COMPILE_DRY_RUN = "compile-dry-run"
    EXECUTE = "execute"

    def __str__(self) -> str:
        return str(self.value)
