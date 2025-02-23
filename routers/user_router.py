from fastapi import APIRouter, Depends, Query, Path
import crud
from schemas.user_schemas import (
    UserCreateSchemas,
    UpdateUserPratialSchemas,
    UpdateUserFullSchemas,
)
from database import get_session
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post("/")
async def create_user(
    user: UserCreateSchemas,
    session: AsyncSession = Depends(get_session),
):
    return await crud.create_user_crud(user=user, session=session)


@router.get("/{user_id}")
async def get_user_by_id(
    user_id: int = Path(..., description="ID пользователя"),
    session: AsyncSession = Depends(get_session),
):
    return await crud.get_user_by_id_crud(user_id=user_id, session=session)


@router.get("/")
async def get_all_users_pagination(
    start: int = Query(..., description="Начальный индекс"),
    stop: int = Query(..., description="Конечный индекс"),
    session: AsyncSession = Depends(get_session),
):
    return await crud.get_all_users_pagination_crud(
        start=start, stop=stop, session=session
    )


@router.patch("/{user_id}")
async def update_user_partial(
    user: UpdateUserPratialSchemas,
    user_id: int,
    session: AsyncSession = Depends(get_session),
):
    return await crud.update_user_partial_crud(
        user=user, user_id=user_id, session=session
    )


@router.put("/{user_id}")
async def update_full_user_info(
    user: UpdateUserFullSchemas,
    user_id: int,
    session: AsyncSession = Depends(get_session),
):
    return await crud.update_user_full_crud(user=user, user_id=user_id, session=session)


@router.delete("/{user_id}")
async def delete_user(user_id: int, session: AsyncSession = Depends(get_session)):
    return await crud.delete_user_crud(user_id=user_id, session=session)
