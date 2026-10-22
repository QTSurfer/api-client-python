from enum import Enum


class LivePaperConfigAccounts(str, Enum):
    CURRENCY = "currency"
    INSTRUMENT = "instrument"

    def __str__(self) -> str:
        return str(self.value)
