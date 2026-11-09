from enum import StrEnum

class ListMyForecastsResponse200DataItemUnscoredReason(StrEnum):
    NO_FRESH_BASELINE = "no_fresh_baseline"

    def __str__(self) -> str:
        return str(self.value)
