from enum import Enum as PyEnum

from sqlalchemy import Column, Date
from sqlalchemy import Enum as SQLEnum
from sqlalchemy import Integer, String

from . import Base


class TaskStatus(PyEnum):
    UNDONE = 1
    DONE = 2


class TaskEntity(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True)
    name = Column(String(1024))
    due_date = Column(Date)
    task_status = Column(SQLEnum(TaskStatus))
    postpone_count = Column(Integer, default=0)
