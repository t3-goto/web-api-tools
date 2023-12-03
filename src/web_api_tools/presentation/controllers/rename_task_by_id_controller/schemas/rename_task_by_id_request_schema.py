from fastapi import Path
from pydantic import BaseModel, Field


# クエリパラメータ用のモデル
class QueryParams(BaseModel):
    pass


# QueryParamsの依存関係を定義
def query_params() -> QueryParams:
    return QueryParams()


# パスパラメータ用のモデル
class PathParams(BaseModel):
    id: int | None = Field(None, example=111)


# PathParamsの依存関係を定義
def path_params(id: int = Path(...)) -> PathParams:
    return PathParams(id=id)


# リクエストボディ用のモデル
class RequestBody(BaseModel):
    name: str | None = Field(None, example="Bob")
