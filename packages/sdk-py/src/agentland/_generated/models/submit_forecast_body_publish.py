from enum import StrEnum

class SubmitForecastBodyPublish(StrEnum):
    CLOSE = "close"
    NEVER = "never"
    RESOLVE = "resolve"

    def __str__(self) -> str:
        return str(self.value)
