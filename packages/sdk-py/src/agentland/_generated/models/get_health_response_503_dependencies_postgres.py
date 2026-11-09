from enum import StrEnum

class GetHealthResponse503DependenciesPostgres(StrEnum):
    OK = "ok"
    UNAVAILABLE = "unavailable"

    def __str__(self) -> str:
        return str(self.value)
