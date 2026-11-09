from enum import StrEnum

class ListQuestionsSort(StrEnum):
    CLOSE_AT = "close_at"
    OPEN_AT = "open_at"
    VALUE_2 = "-open_at"
    VALUE_3 = "-resolved_at"

    def __str__(self) -> str:
        return str(self.value)
