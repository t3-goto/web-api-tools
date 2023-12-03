from datetime import date

from pydantic import BaseModel, Field


# クエリパラメータ用のモデル
class QueryParams(BaseModel):
    pass


# QueryParamsの依存関係を定義
def query_params() -> QueryParams:
    return QueryParams()


# パスパラメータ用のモデル
class PathParams(BaseModel):
    pass


# PathParamsの依存関係を定義
def path_params() -> PathParams:
    return PathParams()


# リクエストボディ用のモデル
class RequestBody(BaseModel):
    name: str | None = Field(None, example="Alex")
    due_date: date | None = Field(None, example="2021-01-01")
