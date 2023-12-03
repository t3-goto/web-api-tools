from pydantic import BaseModel, Field

from .....domain.task.models.task_model import Task


# 基本的な応答スキーマ
class ServiceOutDto(BaseModel):
    task: Task | None = Field(None)
