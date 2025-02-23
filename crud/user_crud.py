from schemas.user_schemas import (
    UserCreateSchemas,
    UserResponseSchemas,
    UpdateUserPratialSchemas,
    UpdateUserFullSchemas,
)
from database import get_session
from fastapi import Depends, HTTPException
from models.user_model import UserOrm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


async def create_user_crud(
    user: UserCreateSchemas,
    session: AsyncSession = Depends(get_session),
    response_model=UserResponseSchemas,
):
    new_user = UserOrm(**user.model_dump())
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return new_user


async def get_user_by_id_crud(
    user_id: int,
    session: AsyncSession = Depends(get_session),
    response_model=UserResponseSchemas,
):
    user = await session.get(UserOrm, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return user


async def get_all_users_pagination_crud(
    start: int,
    stop: int,
    session: AsyncSession = Depends(get_session),
    response_model=list[UserResponseSchemas],
):
    # LIMIT – ограничивает количество возвращаемых строк
    # OFFSET – пропускает N первых строк в выборке
    if start >= stop or start < 0:
        raise HTTPException(status_code=400, detail="Неверные значения пагинации")

    stmt = select(UserOrm).offset(start).limit(stop - start)
    result = await session.execute(stmt)
    users = result.scalars().all()
    return users


async def update_user_partial_crud(
    user: UpdateUserPratialSchemas,
    user_id: int,
    session: AsyncSession = Depends(get_session),
    response_model=UserResponseSchemas,
):
    upd_user = await session.get(UserOrm, user_id)
    if not upd_user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    # exclude_unset=True игнорировать поля, которые не пришли в запросе.
    for key, value in user.model_dump(exclude_unset=True).items():
        setattr(upd_user, key, value)
    await session.commit()
    await session.refresh(upd_user)
    return upd_user


async def update_user_full_crud(
    user: UpdateUserFullSchemas,
    user_id: int,
    session: AsyncSession = Depends(get_session),
    response_model=UserResponseSchemas,
):
    upd_full_user = await session.get(UserOrm, user_id)
    if not upd_full_user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    for key, value in user.model_dump().items():
        setattr(upd_full_user, key, value)
    await session.commit()
    await session.refresh(upd_full_user)
    return upd_full_user


async def delete_user_crud(user_id: int, session: AsyncSession = Depends(get_session)):
    user = await session.get(UserOrm, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    await session.delete(user)
    await session.commit()
    return {"detail": "Пользователь удален"}
