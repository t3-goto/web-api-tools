import logging
import os
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from .presentation.controllers.create_task_controller import (
    create_task_controller,
)
from .presentation.controllers.delete_task_by_id_controller import (
    delete_task_by_id_controller,
)
from .presentation.controllers.done_task_by_id_controller import (
    done_task_by_id_controller,
)
from .presentation.controllers.get_task_by_id_controller import (
    get_task_by_id_controller,
)
from .presentation.controllers.get_tasks_controller import get_tasks_controller
from .presentation.controllers.postpone_task_by_id_controller import (
    postpone_task_by_id_controller,
)
from .presentation.controllers.rename_task_by_id_controller import (
    rename_task_by_id_controller,
)

# プロジェクトのルートディレクトリへのパスを取得
root_dir = Path(__file__).resolve().parents[2]

# .envファイルへのパスを作成
env_path = root_dir / ".env"

# .envファイルを読み込む
load_dotenv(env_path)

app = FastAPI()

# Logging configuration
logging.basicConfig(level=logging.INFO)

# Include routers
routers = [
    get_tasks_controller.router,  # GET /api/v1/tasks
    get_task_by_id_controller.router,  # GET /api/v1/tasks/{id}
    create_task_controller.router,  # POST /api/v1/tasks
    rename_task_by_id_controller.router,  # PUT /api/v1/tasks/{id}/rename
    postpone_task_by_id_controller.router,  # PUT /api/v1/tasks/{id}/postpone
    done_task_by_id_controller.router,  # PUT /api/v1/tasks/{id}/done
    delete_task_by_id_controller.router,  # DELETE /api/v1/tasks/{id}
]

for router in routers:
    app.include_router(router)

# CORS configuration from environment variables
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.environ["ALLOW_ORIGINS"].split(",")
    if "ALLOW_ORIGINS" in os.environ
    else ["*"],
    allow_credentials=True,
    allow_methods=os.environ["ALLOW_METHODS"].split(",")
    if "ALLOW_METHODS" in os.environ
    else ["*"],
    allow_headers=os.environ["ALLOW_HEADERS"].split(",")
    if "ALLOW_HEADERS" in os.environ
    else ["*"],
)


@app.exception_handler(HTTPException)
# Custom HTTP exception handler
async def custom_http_exception_handler(request, exc):
    logging.error(f"An error occurred: {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )
