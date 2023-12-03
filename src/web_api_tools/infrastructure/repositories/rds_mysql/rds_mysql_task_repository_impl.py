from datetime import date

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from ....domain.task.models.task_model import Task, TaskStatus
from ....domain.task.repositories.abstract_task_repository import (
    AbstractTaskRepository,
)
from ....infrastructure.internal_services.rds_mysql import TaskEntity
from ....infrastructure.internal_services.rds_mysql import (
    TaskStatus as EntityTaskStatus,
)


class RdsMysqlTaskRepository(AbstractTaskRepository):
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def find_tasks(self) -> list[Task]:
        result = await self.db_session.execute(select(TaskEntity))
        return [
            self._entity_to_domain(task) for task in result.scalars().all()
        ]

    async def save(self, task: Task) -> Task:
        task_entity = self._domain_to_entity(task)
        self.db_session.add(task_entity)
        await self.db_session.commit()
        await self.db_session.refresh(task_entity)
        return self._entity_to_domain(task_entity)

    async def find_by_id(self, id: int) -> Task:
        result = await self.db_session.execute(
            select(TaskEntity).filter(TaskEntity.id == id)
        )
        task_entity = result.scalars().first()
        if task_entity is None:
            return None
        return self._entity_to_domain(task_entity)

    async def update(self, id: int, task: Task) -> Task:
        result = await self.db_session.execute(
            select(TaskEntity).filter(TaskEntity.id == id)
        )
        task_entity = result.scalars().first()
        if task_entity is None:
            raise ValueError(f"Task with id {id} does not exist")

        for key, value in task.__dict__.items():
            if key != "_sa_instance_state":  # SQLAlchemyの内部状態を除外
                setattr(
                    task_entity, key, self._domain_to_entity_value(key, value)
                )

        await self.db_session.commit()
        await self.db_session.refresh(task_entity)
        return self._entity_to_domain(task_entity)

    async def delete(self, id: int) -> None:
        result = await self.db_session.execute(
            select(TaskEntity).filter(TaskEntity.id == id)
        )
        task_entity = result.scalars().first()
        if task_entity is None:
            raise ValueError(f"Task with id {id} does not exist")

        await self.db_session.delete(task_entity)
        await self.db_session.commit()

    async def find_expired_tasks(self, due_date: date) -> list[Task]:
        result = await self.db_session.execute(
            select(TaskEntity).filter(
                TaskEntity.due_date < due_date,
                TaskEntity.task_status == EntityTaskStatus.UNDONE,
            )
        )
        return [
            self._entity_to_domain(task) for task in result.scalars().all()
        ]

    async def find_in_date_tasks(self, due_date: date) -> list[Task]:
        result = await self.db_session.execute(
            select(TaskEntity).filter(
                TaskEntity.due_date >= due_date,
                TaskEntity.task_status == EntityTaskStatus.UNDONE,
            )
        )
        return [
            self._entity_to_domain(task) for task in result.scalars().all()
        ]

    def _domain_to_entity(self, task: Task) -> TaskEntity:
        return TaskEntity(
            id=task.id,
            name=task.name,
            due_date=task.due_date,
            task_status=EntityTaskStatus(task.task_status.value),
            postpone_count=task.postpone_count,
        )

    def _entity_to_domain(self, task_entity: TaskEntity) -> Task:
        return Task(
            id=task_entity.id,
            name=task_entity.name,
            due_date=task_entity.due_date,
            task_status=TaskStatus(task_entity.task_status.value),  # .valueを追加
            postpone_count=task_entity.postpone_count,
        )

    def _domain_to_entity_value(self, key: str, value: any) -> any:
        if key == "task_status":
            return EntityTaskStatus(value)
        return value
