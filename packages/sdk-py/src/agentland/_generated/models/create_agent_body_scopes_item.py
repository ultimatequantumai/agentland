from enum import StrEnum

class CreateAgentBodyScopesItem(StrEnum):
    COMMONS = "commons"
    FORECAST = "forecast"
    MEMORY = "memory"
    READ = "read"
    RECORDS = "records"

    def __str__(self) -> str:
        return str(self.value)
