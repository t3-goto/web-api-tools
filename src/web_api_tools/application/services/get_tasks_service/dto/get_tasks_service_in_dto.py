from datetime import date

from pydantic import BaseModel, Field


class ServiceInDto(BaseModel):
    due_date: date | None = Field(None, example="2020-01-01")
    expired: bool | None = Field(None, example="True")
