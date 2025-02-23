from sqlalchemy.orm import DeclarativeBase

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker


class Base(DeclarativeBase):
    pass


engine = create_async_engine("sqlite+aiosqlite:///task_manager.db", echo=True)

AsyncSession = async_sessionmaker(bind=engine)


# функция для получения сессии
async def get_session():
    async with AsyncSession() as session:
        yield session
