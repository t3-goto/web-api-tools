from datetime import date, timedelta

import pytest

from src.web_api_tools.domain.task.models.task_model import Task, TaskStatus


# Task インスタンス作成のテスト
def test_create_task_with_valid_data():
    task = Task(id=1, name="Test Task", due_date=date.today())
    assert task.id == 1
    assert task.name == "Test Task"
    assert task.due_date == date.today()
    assert task.task_status == TaskStatus.UNDONE
    assert task.postpone_count == 0


def test_create_task_without_optional_id():
    task = Task(name="Test Task", due_date=date.today())
    assert task.id is None
    assert task.name == "Test Task"
    assert task.due_date == date.today()


def test_create_task_with_invalid_name():
    with pytest.raises(ValueError):
        Task(name="", due_date=date.today())


def test_create_task_with_invalid_due_date():
    with pytest.raises(ValueError):
        Task(name="Test Task", due_date="invalid-date")


# postpone メソッドのテスト
def test_postpone_task_successfully():
    task = Task(name="Test Task", due_date=date.today())
    task.postpone()
    assert task.due_date == date.today() + timedelta(days=1)
    assert task.postpone_count == 1


def test_postpone_task_max_count_reached():
    task = Task(
        name="Test Task",
        due_date=date.today(),
        postpone_count=Task.POSTPONE_MAX_COUNT,
    )
    with pytest.raises(ValueError):
        task.postpone()


# done メソッドのテスト
def test_mark_task_as_done():
    task = Task(name="Test Task", due_date=date.today())
    task.done()
    assert task.task_status == TaskStatus.DONE


# rename メソッドのテスト
def test_rename_task_successfully():
    task = Task(name="Test Task", due_date=date.today())
    new_name = "Updated Task Name"
    task.rename(name=new_name)
    assert task.name == new_name


def test_rename_task_with_empty_name():
    task = Task(name="Test Task", due_date=date.today())
    with pytest.raises(ValueError):
        task.rename(name="")


# can_postpone プロパティのテスト
def test_can_postpone_true():
    task = Task(name="Test Task", due_date=date.today())
    assert task.can_postpone


def test_can_postpone_false():
    task = Task(
        name="Test Task",
        due_date=date.today(),
        postpone_count=Task.POSTPONE_MAX_COUNT,
    )
    assert not task.can_postpone


# バリデーターのテスト
def test_validators_for_required_fields():
    with pytest.raises(ValueError):
        Task(name=None, due_date=None)


def test_name_validator_with_valid_data():
    task = Task(name="Test Task", due_date=date.today())
    assert task.name == "Test Task"


def test_due_date_validator_with_valid_data():
    task = Task(name="Test Task", due_date=date.today())
    assert task.due_date == date.today()


def test_name_validator_with_invalid_type():
    with pytest.raises(ValueError):
        Task(name=123, due_date=date.today())


def test_due_date_validator_with_invalid_type():
    with pytest.raises(ValueError):
        Task(name="Test Task", due_date="invalid-date")
