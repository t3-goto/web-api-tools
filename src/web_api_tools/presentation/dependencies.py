from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ..application.services.create_task_service import (
    CreateTaskApplicationService,
)
from ..application.services.delete_task_by_id_service import (
    DeleteTaskByIdApplicationService,
)
from ..application.services.done_task_by_id_service import (
    DoneTaskByIdApplicationService,
)
from ..application.services.get_task_by_id_service import (
    GetTaskByIdApplicationService,
)
from ..application.services.get_tasks_service import GetTasksApplicationService
from ..application.services.postpone_task_by_id_service import (
    PostponeTaskByIdApplicationService,
)
from ..application.services.rename_task_by_id_service import (
    RenameTaskByIdApplicationService,
)
from ..domain.task.repositories.abstract_task_repository import (
    AbstractTaskRepository,
)
from ..infrastructure.internal_services.rds_mysql import RdsMysqlSessionFactory

# from ..infrastructure.repositories.in_memory import (
#     InMemoryTaskRepository,
# )
from ..infrastructure.repositories.rds_mysql import RdsMysqlTaskRepository


async def get_db_session() -> AsyncSession:
    async with RdsMysqlSessionFactory() as session:
        yield session


# def get_tasks_repository() -> AbstractTaskRepository:
#     return InMemoryTaskRepository()


def get_tasks_repository(
    db: AsyncSession = Depends(get_db_session),
) -> AbstractTaskRepository:
    return RdsMysqlTaskRepository(db_session=db)


def get_get_tasks_application_service(
    task_repository: AbstractTaskRepository = Depends(get_tasks_repository),
) -> GetTasksApplicationService:
    return GetTasksApplicationService(task_repository=task_repository)


def get_get_task_by_id_application_service(
    task_repository: AbstractTaskRepository = Depends(get_tasks_repository),
) -> GetTaskByIdApplicationService:
    return GetTaskByIdApplicationService(task_repository=task_repository)


def get_create_task_application_service(
    task_repository: AbstractTaskRepository = Depends(get_tasks_repository),
) -> CreateTaskApplicationService:
    return CreateTaskApplicationService(task_repository=task_repository)


def get_rename_task_by_id_application_service(
    task_repository: AbstractTaskRepository = Depends(get_tasks_repository),
) -> RenameTaskByIdApplicationService:
    return RenameTaskByIdApplicationService(task_repository=task_repository)


def get_postpone_task_by_id_application_service(
    task_repository: AbstractTaskRepository = Depends(get_tasks_repository),
) -> PostponeTaskByIdApplicationService:
    return PostponeTaskByIdApplicationService(task_repository=task_repository)


def get_done_task_by_id_application_service(
    task_repository: AbstractTaskRepository = Depends(get_tasks_repository),
) -> DoneTaskByIdApplicationService:
    return DoneTaskByIdApplicationService(task_repository=task_repository)


def get_delete_task_by_id_application_service(
    task_repository: AbstractTaskRepository = Depends(get_tasks_repository),
) -> DeleteTaskByIdApplicationService:
    return DeleteTaskByIdApplicationService(task_repository=task_repository)
