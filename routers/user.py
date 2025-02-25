from fastapi import APIRouter, Depends, Query, Path
from schemas.user import (
    UserResponseWithOutRelationship,
    UserCreateSchemas,
    UserResponseSchemas,
    UpdateUserPartialSchemas,
    UpdateUserFullSchemas,
)
import crud
from database import get_session
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post("/", response_model=UserResponseWithOutRelationship)
async def create_user(
    user: UserCreateSchemas, session: AsyncSession = Depends(get_session)
):
    return await crud.create_user_crud(user=user, session=session)


@router.get("/{user_id}", response_model=UserResponseSchemas)
async def get_user_by_id_with_tasks(
    user_id: int = Path(..., description="ID пользователя"),
    session: AsyncSession = Depends(get_session),
):
    return await crud.get_user_by_id_with_tasks_crud(user_id=user_id, session=session)


@router.get("/", response_model=UserResponseSchemas)
async def get_all_users_pagination_with_tasks(
    start: int = Query(..., description="Начальный индекс"),
    stop: int = Query(..., description="Конечный индекс"),
    session: AsyncSession = Depends(get_session),
):
    return await crud.get_all_users_with_tasks_pagination_crud(
        start=start, stop=stop, session=session
    )


@router.patch("/{user_id}", response_model=UserResponseWithOutRelationship)
async def update_user_partial(
    user: UpdateUserPartialSchemas,
    user_id: int = Path(..., description="ID пользователя"),
    session: AsyncSession = Depends(get_session),
):
    return await crud.update_user_partial_crud(
        user=user, user_id=user_id, session=session
    )


@router.put("/{user_id}", response_model=UserResponseWithOutRelationship)
async def update_full_user(
    user: UpdateUserFullSchemas,
    user_id: int,
    session: AsyncSession = Depends(get_session),
):
    return await crud.update_user_full_crud(user=user, user_id=user_id, session=session)
