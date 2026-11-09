from enum import StrEnum

class ListAgentRationalesResponse200DataItemUnscoredReason(StrEnum):
    NO_FRESH_BASELINE = "no_fresh_baseline"

    def __str__(self) -> str:
        return str(self.value)
