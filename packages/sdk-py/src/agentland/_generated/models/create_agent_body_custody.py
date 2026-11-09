from enum import StrEnum

class CreateAgentBodyCustody(StrEnum):
    PLATFORM = "platform"
    SELF = "self"

    def __str__(self) -> str:
        return str(self.value)
