from enum import StrEnum

class ListQuestionsMine(StrEnum):
    FORECASTED = "forecasted"
    NOT_FORECASTED = "not_forecasted"

    def __str__(self) -> str:
        return str(self.value)
