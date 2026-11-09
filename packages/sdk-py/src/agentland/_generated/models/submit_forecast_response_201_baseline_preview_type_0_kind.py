from enum import StrEnum

class SubmitForecastResponse201BaselinePreviewType0Kind(StrEnum):
    COMMUNITY = "community"
    MARKET = "market"

    def __str__(self) -> str:
        return str(self.value)
