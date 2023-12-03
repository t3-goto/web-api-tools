from abc import ABC, abstractmethod
from datetime import date

from ..models.task_model import Task


class AbstractTaskRepository(ABC):
    @abstractmethod
    async def find_tasks(self) -> list[Task]:
        pass

    @abstractmethod
    async def find_by_id(self, id: int) -> Task:
        pass

    @abstractmethod
    async def save(self, task: Task) -> Task:
        pass

    @abstractmethod
    async def update(self, id: int, task: Task) -> Task:
        pass

    @abstractmethod
    async def delete(self, id: int) -> None:
        pass

    @abstractmethod
    async def find_expired_tasks(self, due_date: date) -> list[Task]:
        pass

    @abstractmethod
    async def find_in_date_tasks(self, due_date: date) -> list[Task]:
        pass
