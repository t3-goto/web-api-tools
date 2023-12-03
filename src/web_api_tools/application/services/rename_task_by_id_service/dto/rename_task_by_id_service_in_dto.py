from pydantic import BaseModel, Field


class ServiceInDto(BaseModel):
    id: int | None = Field(None, example=111)
    name: str
