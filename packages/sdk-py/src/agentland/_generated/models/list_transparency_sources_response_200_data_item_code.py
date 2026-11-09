from enum import StrEnum

class ListTransparencySourcesResponse200DataItemCode(StrEnum):
    HOUSE = "house"
    KALSHI = "kalshi"
    POLYMARKET_US = "polymarket_us"

    def __str__(self) -> str:
        return str(self.value)
