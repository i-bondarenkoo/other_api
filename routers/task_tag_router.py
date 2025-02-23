from fastapi import APIRouter
from fastapi import Depends
from database import get_session
from sqlalchemy.ext.asyncio import AsyncSession
import crud

router = APIRouter(prefix="/task_tag", tags=["Task-Tag"])


@router.post("/add")
async def add_data_to_task_tag_table(
    task_id: int, tag_id: int, session: AsyncSession = Depends(get_session)
):
    return await crud.add_task_tag_association(
        task_id=task_id, tag_id=tag_id, session=session
    )


@router.delete("/delete")
async def delete_data_to_task_tag_table(
    task_id: int, tag_id: int, session: AsyncSession = Depends(get_session)
):
    return await crud.delete_data_task_tag_association(
        task_id=task_id, tag_id=tag_id, session=session
    )


@router.get("/all_tasks")
async def get_all_task_by_tag(
    tag_id: int, session: AsyncSession = Depends(get_session)
):
    return await crud.get_all_task_by_tag_association(tag_id=tag_id, session=session)


@router.get("/all_tags")
async def get_all_tags_by_task(
    task_id: int, session: AsyncSession = Depends(get_session)
):
    return await crud.get_all_tags_by_task_association(task_id=task_id, session=session)


@router.get("/associations")
async def get_all_associations(session: AsyncSession = Depends(get_session)):
    return await crud.get_all_tasktags_associations(session=session)
