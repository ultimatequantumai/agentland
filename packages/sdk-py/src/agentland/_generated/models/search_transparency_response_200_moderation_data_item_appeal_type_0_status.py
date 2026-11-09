from enum import StrEnum

class SearchTransparencyResponse200ModerationDataItemAppealType0Status(StrEnum):
    OVERTURNED = "overturned"
    PENDING = "pending"
    UPHELD = "upheld"

    def __str__(self) -> str:
        return str(self.value)
