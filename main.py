from fastapi import FastAPI
import uvicorn
from contextlib import asynccontextmanager
from database import Base, engine
import models
from routers.user import router as user_router

# from routers.task_router import router as task_router
# from routers.tag_router import router as tag_router
# from routers.task_tag_router import router as task_tag_router


# функция для работы с базой данных
@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()


app = FastAPI(lifespan=lifespan)
app.include_router(user_router)
# app.include_router(task_router)
# app.include_router(tag_router)
# app.include_router(task_tag_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
