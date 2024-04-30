from edgegap_scheduling import SchedulingSingleton, Task, errors
from fastapi import (
    FastAPI,
    HTTPException
)
from fastapi.routing import APIRouter


class SchedulingAPI:
    tags = ["Scheduling"]

    def __init__(self):
        self.__instance = SchedulingSingleton.scheduler()

    def init_scheduling_api(self, app: FastAPI):
        router = APIRouter(prefix="/scheduling/tasks", tags=self.tags)

        @router.get("/", description="Get all Tasks")
        async def get_tasks() -> list[Task]:
            return await self.__instance.list()

        @router.get("/{identifier}", description="Get One Task")
        async def get_task(identifier: str) -> Task:
            try:
                return await self.__instance.get(identifier)
            except ValueError as e:
                raise HTTPException(status_code=404, detail=str(e))

        @router.post("/{identifier}", description="Start a stopped Task")
        async def start_task(identifier: str) -> Task:
            try:
                return await self.__instance.start(identifier)
            except ValueError as e:
                raise HTTPException(status_code=404, detail=str(e))

        @router.patch("/{identifier}", description="Update the Interval of a Task")
        async def update_task(identifier: str, every: str | None = None, delay: str | None = None) -> Task:
            try:
                return await self.__instance.update(identifier, every, delay)
            except ValueError as e:
                raise HTTPException(status_code=404, detail=str(e))

        @router.delete("/{identifier}", description="Stop a running Task")
        async def stop_task(identifier: str) -> Task:
            try:
                return await self.__instance.stop(identifier)
            except ValueError as e:
                raise HTTPException(status_code=404, detail=str(e))

        @router.post("/run/{identifier}")
        async def run_rask(identifier: str) -> Task:
            try:
                return await self.__instance.run(identifier)
            except ValueError as e:
                raise HTTPException(status_code=404, detail=str(e))
            except errors.ManualRunNotAllowedError as e:
                raise HTTPException(status_code=403, detail=str(e))

        app.include_router(router)
