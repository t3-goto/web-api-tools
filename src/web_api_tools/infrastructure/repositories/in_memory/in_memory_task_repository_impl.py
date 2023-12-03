from datetime import date

from ....domain.task.models.task_model import Task, TaskStatus
from ....domain.task.repositories.abstract_task_repository import (
    AbstractTaskRepository,
)


class InMemoryTaskRepository(AbstractTaskRepository):
    _instance = None
    _is_initialized = False

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(InMemoryTaskRepository, cls).__new__(
                cls, *args, **kwargs
            )
        return cls._instance

    def __init__(self):
        if not self._is_initialized:
            self._is_initialized = True
            self.tasks = {}
            self.next_id = 1

    async def find_tasks(self) -> list[Task]:
        return list(self.tasks.values())

    async def save(self, task: Task) -> Task:
        if not hasattr(task, "id") or task.id is None:
            task.id = self.next_id
            self.next_id += 1
        self.tasks[task.id] = task
        return task

    async def find_by_id(self, id: int) -> Task:
        for task in self.tasks.values():
            if task.id == id:
                return task
        return None

    async def update(self, id: int, task: Task) -> Task:
        if id not in self.tasks:
            raise ValueError(f"Task with id {id} does not exist")
        self.tasks[id] = task
        return task

    async def delete(self, id: int) -> None:
        if id not in self.tasks:
            raise ValueError(f"Task with id {id} does not exist")
        del self.tasks[id]

    async def find_expired_tasks(self, due_date: date) -> list[Task]:
        return [
            task
            for task in self.tasks.values()
            if task.due_date < due_date
            and task.task_status == TaskStatus.UNDONE
        ]

    async def find_in_date_tasks(self, due_date: date) -> list[Task]:
        return [
            task
            for task in self.tasks.values()
            if task.due_date >= due_date
            and task.task_status == TaskStatus.UNDONE
        ]
