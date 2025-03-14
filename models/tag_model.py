from database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from models.associations import task_tag_table
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.task_model import TaskOrm


class TagOrm(Base):
    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)

    tasks: Mapped[list["TaskOrm"]] = relationship(
        "TaskOrm", secondary=task_tag_table, back_populates="tags"
    )
