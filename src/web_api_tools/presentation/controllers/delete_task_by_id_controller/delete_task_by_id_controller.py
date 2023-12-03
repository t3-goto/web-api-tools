from fastapi import APIRouter, Depends

from ....application.services.delete_task_by_id_service import ServiceInDto
from ...dependencies import (
    get_delete_task_by_id_application_service as get_service,
)
from .schemas import delete_task_by_id_request_schema as request_schema
from .schemas import delete_task_by_id_response_schema as response_schema

router = APIRouter()


@router.delete(
    "/api/v1/tasks/{id}",
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
    # request_body: request_schema.RequestBody = None, # 本エンドポイントでは使用しない
    service=Depends(get_service, use_cache=False),
):
    service_in_dto = ServiceInDto(id=path_params.id)
    await service.execute(service_in_dto)
    response = response_schema.ResponseSchema(
        success=True, data=None, message=None
    )
    return response
