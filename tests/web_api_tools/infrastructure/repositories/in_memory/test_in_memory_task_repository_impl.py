from datetime import date, timedelta

import pytest

from src.web_api_tools.domain.task.models.task_model import Task, TaskStatus
from src.web_api_tools.infrastructure.repositories.in_memory.in_memory_task_repository_impl import (
    InMemoryTaskRepository,
)


@pytest.fixture
async def clean_repository():
    repository = InMemoryTaskRepository()
    # Assuming clear is a method that removes all tasks from the repository
    await repository.clear()
    return repository


@pytest.fixture
def task():
    return Task(
        id=None,
        name="Test Task",
        due_date=date.today(),
        task_status=TaskStatus.UNDONE,
    )


@pytest.mark.asyncio
async def test_singleton():
    repository1 = InMemoryTaskRepository()
    repository2 = InMemoryTaskRepository()
    assert repository1 is repository2


@pytest.mark.asyncio
async def test_save(clean_repository, task):
    repository = await clean_repository
    saved_task = await repository.save(task)
    assert saved_task.id == 1
    assert saved_task.name == "Test Task"


@pytest.mark.asyncio
async def test_find_by_id(clean_repository, task):
    repository = await clean_repository
    saved_task = await repository.save(task)
    found_task = await repository.find_by_id(saved_task.id)
    assert found_task.id == saved_task.id


@pytest.mark.asyncio
async def test_find_by_id_not_found(clean_repository):
    repository = await clean_repository
    assert await repository.find_by_id(999) is None


@pytest.mark.asyncio
async def test_update(clean_repository, task):
    repository = await clean_repository
    saved_task = await repository.save(task)
    saved_task.name = "Updated Task"
    updated_task = await repository.update(saved_task.id, saved_task)
    assert updated_task.name == "Updated Task"


@pytest.mark.asyncio
async def test_update_not_found(clean_repository, task):
    repository = await clean_repository
    with pytest.raises(ValueError):
        await repository.update(999, task)


@pytest.mark.asyncio
async def test_delete(clean_repository, task):
    repository = await clean_repository
    saved_task = await repository.save(task)
    await repository.delete(saved_task.id)
    # Try to delete again
    with pytest.raises(ValueError):
        await repository.delete(saved_task.id)


@pytest.mark.asyncio
async def test_delete_not_found(clean_repository):
    repository = await clean_repository
    with pytest.raises(ValueError):
        await repository.delete(999)


@pytest.mark.asyncio
async def test_find_expired_tasks(clean_repository, task):
    repository = await clean_repository
    task.due_date = date.today() - timedelta(days=1)
    await repository.save(task)
    expired_tasks = await repository.find_expired_tasks(date.today())
    assert len(expired_tasks) == 1


@pytest.mark.asyncio
async def test_find_in_date_tasks(clean_repository):
    repository = await clean_repository
    task = Task(
        id=None,
        name="Test Task",
        due_date=date.today() + timedelta(days=1),
        task_status=TaskStatus.UNDONE,
    )
    await repository.save(task)
    in_date_tasks = await repository.find_in_date_tasks(
        date.today() + timedelta(days=1)
    )
    assert len(in_date_tasks) == 1


@pytest.mark.asyncio
async def test_find_tasks(clean_repository, task):
    repository = await clean_repository
    await repository.clear()  # Ensure the repository is clear before the test
    await repository.save(task)
    tasks = await repository.find_tasks()
    assert len(tasks) == 1


@pytest.mark.asyncio
async def test_save_without_id(clean_repository, task):
    repository = await clean_repository
    task.id = None
    saved_task = await repository.save(task)
    assert saved_task.id is not None
