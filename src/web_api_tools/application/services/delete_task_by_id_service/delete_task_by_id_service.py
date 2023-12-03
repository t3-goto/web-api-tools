from ....domain.task.repositories.abstract_task_repository import (
    AbstractTaskRepository,
)
from .dto.delete_task_by_id_service_in_dto import ServiceInDto
from .dto.delete_task_by_id_service_out_dto import ServiceOutDto


class DeleteTaskByIdApplicationService:
    def __init__(self, task_repository: AbstractTaskRepository):
        self.task_repository = task_repository

    async def execute(self, service_in_dto: ServiceInDto):
        task = await self.task_repository.find_by_id(
            service_in_dto.id
        )  # タスクを非同期的に取得する
        if task is None:
            raise ValueError(
                f"ID {service_in_dto.id} のタスクは存在しません。"
            )  # エラーメッセージを投げる
        await self.task_repository.delete(service_in_dto.id)  # タスクを非同期的に削除する
        service_out_dto = ServiceOutDto()
        return service_out_dto
