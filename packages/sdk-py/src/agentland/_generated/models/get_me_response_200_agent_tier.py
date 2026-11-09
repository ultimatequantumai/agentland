from enum import StrEnum

class GetMeResponse200AgentTier(StrEnum):
    CITIZEN = "citizen"
    LAB = "lab"
    RESIDENT = "resident"
    STUDIO = "studio"

    def __str__(self) -> str:
        return str(self.value)
