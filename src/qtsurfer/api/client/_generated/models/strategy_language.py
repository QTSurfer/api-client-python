from enum import Enum


class StrategyLanguage(str, Enum):
    JAVA = "java"
    QTSCRIPT = "qtscript"

    def __str__(self) -> str:
        return str(self.value)
