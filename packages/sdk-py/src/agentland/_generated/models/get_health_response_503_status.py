from enum import StrEnum

class GetHealthResponse503Status(StrEnum):
    DEGRADED = "degraded"
    OK = "ok"

    def __str__(self) -> str:
        return str(self.value)
