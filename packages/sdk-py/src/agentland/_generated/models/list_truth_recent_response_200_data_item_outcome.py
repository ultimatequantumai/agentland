from enum import StrEnum

class ListTruthRecentResponse200DataItemOutcome(StrEnum):
    NO = "no"
    YES = "yes"

    def __str__(self) -> str:
        return str(self.value)
