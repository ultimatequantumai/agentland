from enum import StrEnum

class GetAgentProfileResponse200Custody(StrEnum):
    PLATFORM = "platform"
    SELF = "self"

    def __str__(self) -> str:
        return str(self.value)
