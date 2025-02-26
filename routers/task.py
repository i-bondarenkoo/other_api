from fastapi import APIRouter, Depends, Query, Path
from database import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.task import (
    FullUpdateTaskSchemas,
    TaskCreateSchemas,
    TaskResponseSchemas,
    TaskResponseSchemasWithOutRelationship,
)
import crud

router = APIRouter(
    prefix="/task",
    tags=["Task"],
)


@router.post("/", response_model=TaskResponseSchemasWithOutRelationship)
async def create_task(
    task: TaskCreateSchemas, session: AsyncSession = Depends(get_session)
):
    return await crud.create_task_crud(task=task, session=session)


@router.get("/", response_model=list[TaskResponseSchemas])
async def get_all_tasks(session: AsyncSession = Depends(get_session)):
    return await crud.get_list_tasks_with_tags_crud(session=session)


@router.get("/{task_id}", response_model=TaskResponseSchemas)
async def get_task_by_id_with_tags(
    task_id: int, session: AsyncSession = Depends(get_session)
):
    return await crud.get_task_by_id_with_tags_crud(task_id=task_id, session=session)


@router.put("/{task_id}", response_model=TaskResponseSchemasWithOutRelationship)
async def update_task(
    task: FullUpdateTaskSchemas,
    task_id: int,
    session: AsyncSession = Depends(get_session),
):
    return await crud.full_update_task_crud(
        task=task,
        task_id=task_id,
        session=session,
    )


@router.delete("/{task_id}")
async def delete_task(task_id: int, session: AsyncSession = Depends(get_session)):
    return await crud.delete_task_crud(task_id=task_id, session=session)
