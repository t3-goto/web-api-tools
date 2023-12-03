from datetime import date

from pydantic import BaseModel, Field


class ServiceInDto(BaseModel):
    name: str | None = Field(None, example="Alex")
    due_date: date | None = Field(None, example="2021-01-01")
