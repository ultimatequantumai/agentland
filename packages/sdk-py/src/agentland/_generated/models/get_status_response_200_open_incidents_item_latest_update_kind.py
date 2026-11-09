from enum import StrEnum

class GetStatusResponse200OpenIncidentsItemLatestUpdateKind(StrEnum):
    NOTICE = "notice"
    POSTMORTEM = "postmortem"
    UPDATE = "update"

    def __str__(self) -> str:
        return str(self.value)
