from enum import StrEnum

class CreateAgentResponse201ScoutType0Status(StrEnum):
    ELIGIBLE = "eligible"
    SAME_OPERATOR = "same_operator"
    SCOUT_UNAVAILABLE = "scout_unavailable"

    def __str__(self) -> str:
        return str(self.value)
