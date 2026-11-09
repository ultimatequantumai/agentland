from enum import StrEnum

class IssueAgentKeyBodyScopesItem(StrEnum):
    COMMONS = "commons"
    FORECAST = "forecast"
    MEMORY = "memory"
    READ = "read"
    RECORDS = "records"

    def __str__(self) -> str:
        return str(self.value)
