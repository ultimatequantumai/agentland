from enum import StrEnum

class ListAgentForecastsStatus(StrEnum):
    CLOSED = "closed"
    OPEN = "open"
    RESOLVED = "resolved"
    VOIDED = "voided"

    def __str__(self) -> str:
        return str(self.value)
