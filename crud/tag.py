from sqlalchemy.ext.asyncio import AsyncSession
from schemas.tag import CreateTagSchemas, FullUpdateTagSchemas
from models.tag import TagOrm
from models.task import TaskOrm
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from fastapi import HTTPException


async def create_tag_crud(tag: CreateTagSchemas, session: AsyncSession):
    new_tag = TagOrm(**tag.model_dump())
    session.add(new_tag)
    await session.commit()
    await session.refresh(new_tag)
    return new_tag


async def get_tag_by_id_with_task_and_user_crud(tag_id: int, session: AsyncSession):
    stmt = (
        select(TagOrm)
        .where(TagOrm.id == tag_id)
        .options(selectinload(TagOrm.tasks).selectinload(TaskOrm.user))
    )
    result = await session.execute(stmt)
    tag_with_tasks_and_user = result.scalars().first()
    if not tag_with_tasks_and_user:
        raise HTTPException(status_code=404, detail="Тег не найден")
    return tag_with_tasks_and_user


async def get_list_tags_and_tasks_crud(session: AsyncSession):
    stmt = select(TagOrm).options(selectinload(TagOrm.tasks))
    result = await session.execute(stmt)
    list_tags_and_tasks = result.scalars().all()
    if not list_tags_and_tasks:
        raise HTTPException(status_code=404, detail="Список тегов и задач пуст!")
    return list_tags_and_tasks


async def update_tag_crud(
    tag: FullUpdateTagSchemas, tag_id: int, session: AsyncSession
):
    tag_upd = await session.get(TagOrm, tag_id)
    if not tag_upd:
        raise HTTPException(status_code=404, detail="Тег не найден")
    for key, value in tag.model_dump().items():
        setattr(tag_upd, key, value)
    await session.commit()
    await session.refresh(tag_upd)
    return tag_upd


async def delete_tag_crud(tag_id: int, session: AsyncSession):
    tag = await session.get(TagOrm, tag_id)
    if not tag:
        raise HTTPException(status_code=404, detail="Тег не найден")
    await session.delete(tag)
    await session.commit()
    return {"message": "Тег был удален!"}
