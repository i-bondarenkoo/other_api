from fastapi import APIRouter, Depends, Query, Path
from database import get_session
from sqlalchemy.ext.asyncio import AsyncSession
import crud
from schemas.task_schemas import (
    TaskCreateSchemas,
    FullUpdateTaskSchemas,
)

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)


@router.post("/")
async def create_task(
    task: TaskCreateSchemas, session: AsyncSession = Depends(get_session)
):
    return await crud.create_task_crud(task=task, session=session)


@router.get("/")
async def get_all_tasks(
    start: int = Query(..., description="Начальные индекс"),
    stop: int = Query(..., description="Конечный индекс"),
    session: AsyncSession = Depends(get_session),
):
    return await crud.get_all_tasks_crud(start=start, stop=stop, session=session)


@router.get("/{task_id}")
async def get_task_by_id(
    task_id: int = Path(..., description="ID задачи"),
    session: AsyncSession = Depends(get_session),
):
    return await crud.get_task_by_id_crud(task_id=task_id, session=session)


@router.put("/{task_id}")
async def update_full_task(
    task_upd: FullUpdateTaskSchemas,
    task_id: int,
    session: AsyncSession = Depends(get_session),
):
    return await crud.full_update_task_crud(
        task_upd=task_upd, task_id=task_id, session=session
    )


@router.delete("/{task_id}")
async def delete_task(task_id: int, session: AsyncSession = Depends(get_session)):
    return await crud.delete_task_crud(task_id=task_id, session=session)
