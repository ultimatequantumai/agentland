from enum import StrEnum

class ListAgentResolvedResponse200DataItemOutcome(StrEnum):
    NO = "no"
    YES = "yes"

    def __str__(self) -> str:
        return str(self.value)
