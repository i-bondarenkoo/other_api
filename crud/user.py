from sqlalchemy.ext.asyncio import AsyncSession
from schemas.user import (
    UserCreateSchemas,
    UpdateUserFullSchemas,
    UpdateUserPartialSchemas,
    UserResponseSchemas,
)
from models.user import UserOrm
from models.task import TaskOrm
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from fastapi import HTTPException


async def create_user_crud(user: UserCreateSchemas, session: AsyncSession):
    new_user = UserOrm(**user.model_dump())
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return new_user


async def check_user_exists(user_id: int, session: AsyncSession):
    result = await session.execute(select(UserOrm.id).where(UserOrm.id == user_id))
    check_user = result.scalars().first()
    if not check_user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return check_user


async def get_user_by_id_with_tasks_crud(user_id: int, session: AsyncSession):
    stmt = (
        select(UserOrm)
        .where(UserOrm.id == user_id)
        .options(selectinload(UserOrm.tasks).selectinload(TaskOrm.tags))
    )
    result = await session.execute(stmt)
    user_with_tasks = result.scalars().first()
    if not user_with_tasks:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return user_with_tasks


async def get_all_users_with_tasks_pagination_crud(
    session: AsyncSession, start=int, stop=int
):
    if start >= stop or start < 0:
        raise HTTPException(status_code=400, detail="Неверные значения пагинации")
    stmt = (
        select(UserOrm)
        .offset(start)
        .limit(stop - start)
        .options(selectinload(UserOrm.tasks).selectinload(TaskOrm.tags))
    )
    result = await session.execute(stmt)
    users_with_tasks_pagination = result.scalars().all()
    if not users_with_tasks_pagination:
        raise HTTPException(status_code=404, detail="Пользователи не найдены")
    return users_with_tasks_pagination


async def update_user_partial_crud(
    user: UpdateUserPartialSchemas,
    user_id: int,
    session: AsyncSession,
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
    session: AsyncSession,
):
    upd_full_user = await session.get(UserOrm, user_id)
    if not upd_full_user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    for key, value in user.model_dump().items():
        setattr(upd_full_user, key, value)
    await session.commit()
    await session.refresh(upd_full_user)
    return upd_full_user


async def delete_user_crud(user_id: int, session: AsyncSession):
    user = await session.get(UserOrm, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    await session.delete(user)
    await session.commit()
    return {"detail": "Пользователь удален"}
