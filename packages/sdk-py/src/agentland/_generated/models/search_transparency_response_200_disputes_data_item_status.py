from enum import StrEnum

class SearchTransparencyResponse200DisputesDataItemStatus(StrEnum):
    OPEN = "open"
    REJECTED = "rejected"
    UPHELD = "upheld"
    VOIDED_QUESTION = "voided_question"

    def __str__(self) -> str:
        return str(self.value)
