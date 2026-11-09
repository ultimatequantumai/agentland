from enum import StrEnum

class GetHealthResponse503DependenciesRedis(StrEnum):
    OK = "ok"
    UNAVAILABLE = "unavailable"

    def __str__(self) -> str:
        return str(self.value)
