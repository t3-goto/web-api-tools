# flake8: noqa: E501
# TODO: 未実装
# FAILED tests/web_api_tools/presentation/controllers/create_task_controller/test_create_task_controller.py::test_create_task_success - sqlalchemy.exc.OperationalError: (asyncmy.errors.OperationalError) (2003, "Can't connect to MySQL server on 'None'...
# FAILED tests/web_api_tools/presentation/controllers/create_task_controller/test_create_task_controller.py::test_create_task_failure - pydantic_core._pydantic_core.ValidationError: 1 validation error for Task

# import pytest
# from fastapi import FastAPI, HTTPException
# from httpx import AsyncClient
# from src.web_api_tools.presentation.controllers.create_task_controller.create_task_controller import router
# from src.web_api_tools.application.services.create_task_service.dto.create_task_service_out_dto import ServiceOutDto
# from src.web_api_tools.domain.task.models.task_model import Task
# from unittest.mock import AsyncMock, patch

# app = FastAPI()
# app.include_router(router)

# # 正常系
# @pytest.mark.asyncio
# async def test_create_task_success():
#     async with AsyncClient(app=app, base_url="http://test") as ac:
#         with patch('src.web_api_tools.presentation.controllers.create_task_controller.create_task_controller.get_service', new_callable=AsyncMock) as mock_service:
#             mock_service.return_value.execute.return_value = ServiceOutDto(task=Task(name="test", due_date="2022-12-31"))
#             response = await ac.post("/api/v1/tasks", json={"name": "test", "due_date": "2022-12-31"})
#             assert response.status_code == 200
#             assert response.json() == {"success": True, "data": {"name": "test", "due_date": "2022-12-31"}, "message": None}

# # 異常系
# @pytest.mark.asyncio
# async def test_create_task_failure():
#     async with AsyncClient(app=app, base_url="http://test") as ac:
#         with patch('src.web_api_tools.presentation.controllers.create_task_controller.create_task_controller.get_service', new_callable=AsyncMock) as mock_service:
#             mock_service.return_value.execute.side_effect = HTTPException(status_code=400, detail="Invalid input")
#             response = await ac.post("/api/v1/tasks", json={"name": "", "due_date": "2022-12-31"})
#             assert response.status_code == 400
#             assert response.json() == {"detail": "Invalid input"}
