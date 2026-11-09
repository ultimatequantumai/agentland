from enum import StrEnum

class GetPublicForecastsResponse200DataItemRationaleType0Publish(StrEnum):
    CLOSE = "close"
    NEVER = "never"
    RESOLVE = "resolve"

    def __str__(self) -> str:
        return str(self.value)
