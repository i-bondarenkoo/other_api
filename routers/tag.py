from sqlalchemy.ext.asyncio import AsyncSession
from models.tag import TagOrm
from models.task import TaskOrm
from database import get_session
from fastapi import APIRouter, Depends
from schemas.tag import (
    ResponseTagWithOutRelationship,
    CreateTagSchemas,
    ResponseTagWithUserAndTask,
    ResponseTagSchemas,
    FullUpdateTagSchemas,
)
import crud

router = APIRouter(
    prefix="/tags",
    tags=["Tags"],
)


@router.post("/", response_model=ResponseTagWithOutRelationship)
async def create_tag(
    tag: CreateTagSchemas, session: AsyncSession = Depends(get_session)
):
    return await crud.create_tag_crud(tag=tag, session=session)


@router.get("/{tag_id}/task-tag", response_model=ResponseTagSchemas)
async def get_tag_by_id_with_user_and_task(
    tag_id: int, session: AsyncSession = Depends(get_session)
):
    return await crud.get_tag_by_id_with_task_and_user_crud(
        tag_id=tag_id, session=session
    )


@router.get("/", response_model=list[ResponseTagSchemas])
async def get_list_tags_and_tasks(session: AsyncSession = Depends(get_session)):
    return await crud.get_list_tags_and_tasks_crud(session=session)


@router.put("/", response_model=ResponseTagWithOutRelationship)
async def update_tag(
    tag: FullUpdateTagSchemas, tag_id: int, session: AsyncSession = Depends(get_session)
):
    return await crud.update_tag_crud(tag=tag, tag_id=tag_id, session=session)


@router.delete("/{tag_id}")
async def delete_tag(tag_id: int, session: AsyncSession = Depends(get_session)):
    return await crud.delete_tag_crud(tag_id=tag_id, session=session)
