from enum import StrEnum

class ListIncidentsResponse200DataItemUpdatesItemKind(StrEnum):
    NOTICE = "notice"
    POSTMORTEM = "postmortem"
    RESOLVED = "resolved"
    UPDATE = "update"

    def __str__(self) -> str:
        return str(self.value)
