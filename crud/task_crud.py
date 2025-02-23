from schemas.task_schemas import (
    TaskCreateSchemas,
    TaskResponseSchemas,
    FullUpdateTaskSchemas,
)
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, HTTPException
from database import get_session
from models.task_model import TaskOrm
from models.user_model import UserOrm
from sqlalchemy import select


async def create_task_crud(
    task: TaskCreateSchemas,
    session: AsyncSession = Depends(get_session),
    response_model=TaskResponseSchemas,
):
    user = await session.get(UserOrm, task.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    new_task = TaskOrm(**task.model_dump())
    session.add(new_task)
    await session.commit()
    await session.refresh(new_task)
    return new_task


async def get_task_by_id_crud(task_id: int, session: AsyncSession):
    task = await session.get(TaskOrm, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return task


async def get_all_tasks_crud(
    start: int = 0,
    stop: int = 5,
    session: AsyncSession = Depends(get_session),
    response_model=list[TaskResponseSchemas],
):
    if start >= stop or start < 0:
        raise HTTPException(status_code=400, detail="Неверные значения пагинации")
    stmt = select(TaskOrm).offset(start).limit(stop - start)
    result = await session.execute(stmt)
    tasks = result.scalars().all()
    return tasks


async def full_update_task_crud(
    task_upd: FullUpdateTaskSchemas,
    task_id: int,
    session: AsyncSession = Depends(get_session),
    response_model=FullUpdateTaskSchemas,
):
    user = await session.get(UserOrm, task_upd.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    task_in_db = await session.get(TaskOrm, task_id)
    if not task_in_db:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    for key, value in task_upd.model_dump().items():
        setattr(task_in_db, key, value)
    await session.commit()
    await session.refresh(task_in_db)
    return task_in_db


async def delete_task_crud(
    task_id: int,
    session: AsyncSession = Depends(get_session),
):
    task_delete = await session.get(TaskOrm, task_id)
    if not task_delete:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    await session.delete(task_delete)
    await session.commit()
    return {"detail": "Задача удалена"}
