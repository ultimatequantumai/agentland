from enum import StrEnum

class GetSeriesResponse200InstancesItemOutcomeType1(StrEnum):
    NO = "no"
    YES = "yes"

    def __str__(self) -> str:
        return str(self.value)
