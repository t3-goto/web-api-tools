from ....domain.task.repositories.abstract_task_repository import (
    AbstractTaskRepository,
)
from .dto.get_task_by_id_service_in_dto import ServiceInDto  # InDtoのインポート
from .dto.get_task_by_id_service_out_dto import ServiceOutDto  # OutDtoのインポート


class GetTaskByIdApplicationService:
    def __init__(self, task_repository: AbstractTaskRepository):
        self.task_repository = task_repository

    async def execute(self, service_in_dto: ServiceInDto):
        task = await self.task_repository.find_by_id(
            service_in_dto.id
        )  # タスクを非同期的に取得する
        service_out_dto = ServiceOutDto(task=task)
        return service_out_dto  # outDtoを返す
