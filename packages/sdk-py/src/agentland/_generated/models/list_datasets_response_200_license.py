from enum import StrEnum

class ListDatasetsResponse200License(StrEnum):
    CC_BY_4_0 = "CC-BY-4.0"

    def __str__(self) -> str:
        return str(self.value)
