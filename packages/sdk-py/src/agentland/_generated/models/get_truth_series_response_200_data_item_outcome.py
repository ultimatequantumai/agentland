from enum import StrEnum

class GetTruthSeriesResponse200DataItemOutcome(StrEnum):
    NO = "no"
    YES = "yes"

    def __str__(self) -> str:
        return str(self.value)
