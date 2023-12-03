from datetime import date

from fastapi import Query
from pydantic import BaseModel, Field


# クエリパラメータ用のモデル
class QueryParams(BaseModel):
    due_date: date | None = Field(None, example="2020-01-01")
    expired: bool | None = Field(None, example="True")


# QueryParamsの依存関係を定義
def query_params(
    due_date: date = Query(None), expired: bool = Query(None)
) -> QueryParams:
    return QueryParams(due_date=due_date, expired=expired)


# パスパラメータ用のモデル
class PathParams(BaseModel):
    pass


# PathParamsの依存関係を定義
def path_params() -> PathParams:
    return PathParams()


# リクエストボディ用のモデル
class RequestBody(BaseModel):
    pass
