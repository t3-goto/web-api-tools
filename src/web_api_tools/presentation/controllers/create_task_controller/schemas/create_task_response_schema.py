from typing import Generic, TypeVar

from pydantic import BaseModel, Field

from .....domain.task.models.task_model import Task

T = TypeVar("T")


# 基本的な応答スキーマ
class BaseResponseSchema(BaseModel, Generic[T]):
    success: bool = Field(None)
    data: T | None = Field(None)
    errors: list[str] | None = Field(None)
    message: str | None = Field(None)

    class Config:
        response_model_exclude_none = True  # None値を持つフィールドを除外


class ResponseSchema(BaseResponseSchema[Task]):
    data: Task | None
