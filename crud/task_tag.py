# from sqlalchemy import select, insert, update, delete
# from models.associations import task_tag_table
# from models.tag_model import TagOrm
# from models.task_model import TaskOrm
# from fastapi import Depends, HTTPException
# from database import get_session
# from sqlalchemy.ext.asyncio import AsyncSession
# from crud.task_crud import get_task_by_id_crud
# from crud.tag_crud import get_tag_by_id_crud
# from sqlalchemy.orm import selectinload


# async def add_task_tag_association(
#     task_id: int, tag_id: int, session: AsyncSession = Depends(get_session)
# ):
#     task = await get_task_by_id_crud(task_id, session)
#     tag = await get_tag_by_id_crud(tag_id, session)

#     stmt = insert(task_tag_table).values(task_id=task.id, tag_id=tag.id)
#     await session.execute(stmt)
#     await session.commit()
#     return {"message": "Данные успешно добавлены"}


# async def delete_data_task_tag_association(
#     task_id: int, tag_id: int, session: AsyncSession = Depends(get_session)
# ):
#     task = await get_task_by_id_crud(task_id, session)
#     tag = await get_tag_by_id_crud(tag_id, session)

#     stmt = delete(task_tag_table).where(
#         task_tag_table.c.task_id == task.id,
#         task_tag_table.c.tag_id == tag.id,
#     )
#     await session.execute(stmt)
#     await session.commit()
#     return {"message": "Данные успешно удалены"}


# async def get_all_tags_by_task_association(
#     task_id: int, session: AsyncSession = Depends(get_session)
# ):
#     stmt = (
#         select(TagOrm)  # Мы выбираем теги
#         .join(
#             task_tag_table, task_tag_table.c.tag_id == TagOrm.id
#         )  # Соединяем с ассоциативной таблицей
#         .where(task_tag_table.c.task_id == task_id)  # Фильтруем по task_id
#     )
#     result = await session.execute(stmt)
#     tags = result.scalars().all()  # Получаем все теги для задачи
#     return tags


# async def get_all_task_by_tag_association(
#     tag_id: int, session: AsyncSession = Depends(get_session)
# ):
#     stmt = (
#         select(TaskOrm)
#         .join(task_tag_table, task_tag_table.c.task_id == TaskOrm.id)
#         .where(task_tag_table.c.tag_id == tag_id)
#     )
#     result = await session.execute(stmt)
#     tasks = result.scalars().all()
#     return tasks


# # Получение всех ассоциаций
# # Функция для получения всех записей из ассоциативной таблицы, то есть всех связок "задача-тег".
# # Она возвращает полный список всех связей, которые существуют в системе.
# # Это может быть полезно, если вам нужно получить полный обзор всех задач с их тегами.


# async def get_all_tasktags_associations(session: AsyncSession = Depends(get_session)):
#     stmt = (
#         select(TaskOrm, TagOrm)
#         .join(
#             task_tag_table, TaskOrm.id == task_tag_table.c.task_id
#         )  # Связь задач с таблицей связей
#         .join(
#             TagOrm, TagOrm.id == task_tag_table.c.tag_id
#         )  # Связь тегов с таблицей связей
#     )

#     result = await session.execute(stmt)
#     tasktags = result.scalars().all()
#     return tasktags


# # Проверка существования ассоциации
# # Функция, которая проверяет, существует ли уже связь между задачей и тегом.
# # Она просто выполняет запрос на проверку, есть ли такая запись в ассоциативной таблице.
# # Это можно использовать перед добавлением новой ассоциации, чтобы избежать дублирования.
