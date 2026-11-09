from enum import StrEnum

class GetStatusResponse200ChecksItemName(StrEnum):
    API = "API"
    CHARTER = "Charter"
    MCP = "MCP"
    WEBSITE = "Website"

    def __str__(self) -> str:
        return str(self.value)
