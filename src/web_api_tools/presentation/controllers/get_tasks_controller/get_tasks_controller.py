from fastapi import APIRouter, Depends

from ....application.services.get_tasks_service import ServiceInDto
from ...dependencies import get_get_tasks_application_service as get_service
from .schemas import get_tasks_request_schema as request_schema
from .schemas import get_tasks_response_schema as response_schema

router = APIRouter()


@router.get(
    "/api/v1/tasks",
    response_model=response_schema.ResponseSchema,
    response_model_exclude_none=True,
)
async def execute(
    path_params: request_schema.PathParams = Depends(
        request_schema.path_params
    ),
    query_params: request_schema.QueryParams = Depends(
        request_schema.query_params
    ),
    # request_body: request_schema.RequestBody = None, # GETメソッドでは使用しない
    service=Depends(get_service, use_cache=False),
):
    service_in_dto = ServiceInDto(
        due_date=query_params.due_date, expired=query_params.expired
    )
    service_out_dto = await service.execute(service_in_dto)
    response = response_schema.ResponseSchema(
        success=True,
        data=[task.dict() for task in service_out_dto.tasks],
        message=None,
    )
    return response
