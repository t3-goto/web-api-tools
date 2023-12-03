from ....domain.task.repositories.abstract_task_repository import (
    AbstractTaskRepository,
)
from .dto.done_task_by_id_service_in_dto import ServiceInDto  # InDtoのインポート
from .dto.done_task_by_id_service_out_dto import ServiceOutDto  # OutDtoのインポート


class DoneTaskByIdApplicationService:
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
        task.done()
        await self.task_repository.update(
            service_in_dto.id, task
        )  # 更新したタスクを非同期的に保存する
        service_out_dto = ServiceOutDto(task=task)
        return service_out_dto  # outDtoを返す
