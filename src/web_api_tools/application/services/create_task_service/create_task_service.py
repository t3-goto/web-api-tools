from ....domain.task.models.task_model import Task
from ....domain.task.repositories.abstract_task_repository import (
    AbstractTaskRepository,
)
from .dto.create_task_service_in_dto import ServiceInDto
from .dto.create_task_service_out_dto import ServiceOutDto


class CreateTaskApplicationService:
    def __init__(self, task_repository: AbstractTaskRepository):
        self.task_repository = task_repository

    async def execute(self, service_in_dto: ServiceInDto):
        task = Task(name=service_in_dto.name, due_date=service_in_dto.due_date)
        saved_task = await self.task_repository.save(task)  # タスクを非同期的に保存する
        service_out_dto = ServiceOutDto(task=saved_task)
        return service_out_dto
