from ....domain.task.repositories.abstract_task_repository import (
    AbstractTaskRepository,
)
from .dto.get_tasks_service_in_dto import ServiceInDto  # InDtoのインポート
from .dto.get_tasks_service_out_dto import ServiceOutDto  # OutDtoのインポート


class GetTasksApplicationService:
    def __init__(self, task_repository: AbstractTaskRepository):
        self.task_repository = task_repository

    async def execute(self, service_in_dto: ServiceInDto):
        if service_in_dto.due_date is None and service_in_dto.expired is None:
            tasks = await self.task_repository.find_tasks()
        elif (
            service_in_dto.due_date is not None
            and service_in_dto.expired is not None
        ):
            if service_in_dto.expired:
                tasks = await self.task_repository.find_expired_tasks(
                    service_in_dto.due_date
                )
            else:
                tasks = await self.task_repository.find_in_date_tasks(
                    service_in_dto.due_date
                )
        else:
            raise ValueError("due_dateとexpiredの両方がNoneであってはなりません。")

        service_out_dto = ServiceOutDto(tasks=tasks)
        return service_out_dto  # outDtoを返す
