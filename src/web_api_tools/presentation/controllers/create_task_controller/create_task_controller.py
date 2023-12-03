from fastapi import APIRouter, Depends

from ....application.services.create_task_service import ServiceInDto
from ...dependencies import get_create_task_application_service as get_service
from .schemas import create_task_request_schema as request_schema
from .schemas import create_task_response_schema as response_schema

router = APIRouter()


@router.post(
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
    request_body: request_schema.RequestBody = None,
    service=Depends(get_service, use_cache=False),
):
    service_in_dto = ServiceInDto(
        name=request_body.name, due_date=request_body.due_date
    )
    service_out_dto = await service.execute(service_in_dto)
    # print()
    response = response_schema.ResponseSchema(
        success=True, data=service_out_dto.task, message=None
    )
    return response
