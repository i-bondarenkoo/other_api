from fastapi import APIRouter, Depends, Query, Path
from database import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.tag_schemas import (
    CreateTagSchemas,
    FullUpdateTagSchemas,
)
import crud

router = APIRouter(prefix="/tags", tags=["Tags"])


@router.post("/")
async def create_tag(
    tag: CreateTagSchemas, session: AsyncSession = Depends(get_session)
):
    return await crud.create_tag_crud(tag=tag, session=session)


@router.get("/{tag_id}")
async def get_tag_by_id(tag_id: int, session: AsyncSession = Depends(get_session)):
    return await crud.get_tag_by_id_crud(tag_id=tag_id, session=session)


@router.put("/{tag_id}")
async def update_tag(
    tag_id: int,
    tag_upd: FullUpdateTagSchemas,
    session: AsyncSession = Depends(get_session),
):
    return await crud.update_tag_crud(tag_id=tag_id, tag_upd=tag_upd, session=session)


@router.delete("/{tag_id}")
async def delete_tag(tag_id: int, session: AsyncSession = Depends(get_session)):
    return await crud.delete_tag_crud(tag_id=tag_id, session=session)
