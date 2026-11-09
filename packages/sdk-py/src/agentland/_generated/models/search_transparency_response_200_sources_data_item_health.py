from enum import StrEnum

class SearchTransparencyResponse200SourcesDataItemHealth(StrEnum):
    HEALTHY = "healthy"
    NO_EVIDENCE = "no_evidence"
    UNHEALTHY = "unhealthy"

    def __str__(self) -> str:
        return str(self.value)
