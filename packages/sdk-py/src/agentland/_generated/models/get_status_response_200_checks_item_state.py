from enum import StrEnum

class GetStatusResponse200ChecksItemState(StrEnum):
    FAILING = "failing"
    NO_DATA = "no_data"
    PASSING = "passing"

    def __str__(self) -> str:
        return str(self.value)
