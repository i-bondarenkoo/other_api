from schemas.task import TaskCreateSchemas, FullUpdateTaskSchemas
from sqlalchemy.ext.asyncio import AsyncSession
from models.task import TaskOrm
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from crud.user import check_user_exists


async def create_task_crud(task: TaskCreateSchemas, session: AsyncSession):
    user = await check_user_exists(task.user_id, session)
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    new_task = TaskOrm(**task.model_dump())
    session.add(new_task)
    await session.commit()
    await session.refresh(new_task)
    return new_task


async def get_task_by_id_with_tags_crud(task_id: int, session: AsyncSession):
    stmt = (
        select(TaskOrm).where(TaskOrm.id == task_id).options(selectinload(TaskOrm.tags))
    )
    result = await session.execute(stmt)
    task_with_tags = result.scalars().first()
    if not task_with_tags:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return task_with_tags


async def get_list_tasks_with_tags_crud(session: AsyncSession):
    stmt = select(TaskOrm).options(selectinload(TaskOrm.tags))
    result = await session.execute(stmt)
    list_tasks_with_tags = result.scalars().all()
    if not list_tasks_with_tags:
        raise HTTPException(status_code=404, detail="Список задач и тэгов пуст!")
    return list_tasks_with_tags


async def full_update_task_crud(
    task: FullUpdateTaskSchemas, task_id: int, session: AsyncSession
):
    user = await check_user_exists(task.user_id, session)
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    task_upd = await session.get(TaskOrm, task_id)
    if not task_upd:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    for key, value in task.model_dump().items():
        setattr(task_upd, key, value)
    await session.commit()
    await session.refresh(task_upd)
    return task_upd


async def delete_task_crud(task_id: int, session: AsyncSession):
    task = await session.get(TaskOrm, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    await session.delete(task)
    await session.commit()
    return {"message": "Задача была удалена!"}
