from datetime import date, timedelta
from enum import IntEnum
from typing import ClassVar, Optional

from pydantic import BaseModel, field_validator


class TaskStatus(IntEnum):
    UNDONE = 1
    DONE = 2


class Task(BaseModel):
    id: Optional[int] = None
    name: str
    due_date: date
    task_status: TaskStatus = TaskStatus.UNDONE
    postpone_count: int = 0
    POSTPONE_MAX_COUNT: ClassVar[int] = 3

    @field_validator("name", "due_date")
    def validate_required(cls, v):
        if not v:
            raise ValueError("必須項目が設定されていません")
        return v

    def postpone(self):
        if self.postpone_count >= self.POSTPONE_MAX_COUNT:
            raise ValueError("最大延期回数を超過しています")

        self.due_date += timedelta(days=1)
        self.postpone_count += 1

    def done(self):
        self.task_status = TaskStatus.DONE

    def rename(self, name: str):
        if not name:
            raise ValueError("必須項目が設定されていません")
        self.name = name

    @property
    def can_postpone(self):
        return self.postpone_count < self.POSTPONE_MAX_COUNT
