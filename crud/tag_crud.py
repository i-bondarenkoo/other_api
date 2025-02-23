from database import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.tag_schemas import (
    CreateTagSchemas,
    ResponseTagSchemas,
    FullUpdateTagSchemas,
)
from fastapi import Depends, HTTPException
from models.tag_model import TagOrm


async def create_tag_crud(
    tag: CreateTagSchemas,
    session: AsyncSession = Depends(get_session),
    response_model=ResponseTagSchemas,
):
    new_tag = TagOrm(**tag.model_dump())
    session.add(new_tag)
    await session.commit()
    await session.refresh(new_tag)
    return new_tag


async def get_tag_by_id_crud(
    tag_id: int,
    session: AsyncSession = Depends(get_session),
    response_model=ResponseTagSchemas,
):
    tag = await session.get(TagOrm, tag_id)
    if not tag:
        raise HTTPException(status_code=404, detail="Тег не найден")
    return tag


async def update_tag_crud(
    tag_id: int,
    tag_upd: FullUpdateTagSchemas,
    session: AsyncSession = Depends(get_session),
    response_model=ResponseTagSchemas,
):
    tag = await session.get(TagOrm, tag_id)
    if not tag:
        raise HTTPException(status_code=404, detail="Тэг не найден")
    for key, value in tag_upd.model_dump().items():
        setattr(tag, key, value)
    await session.commit()
    await session.refresh(tag)
    return tag


async def delete_tag_crud(
    tag_id: int,
    session: AsyncSession = Depends(get_session),
):
    delete_tag = await session.get(TagOrm, tag_id)
    if not delete_tag:
        raise HTTPException(status_code=404, detail="Тег не найден")
    await session.delete(delete_tag)
    await session.commit()
    return {"message": "Тэг успешно удален"}
