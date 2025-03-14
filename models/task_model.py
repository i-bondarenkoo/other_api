from database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from sqlalchemy import ForeignKey
from models.associations import task_tag_table
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.tag_model import TagOrm
    from models.user_model import UserOrm


class TaskOrm(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(30))
    description: Mapped[str] = mapped_column(String(100))

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    user: Mapped["UserOrm"] = relationship("UserOrm", back_populates="tasks")

    tags: Mapped[list["TagOrm"]] = relationship(
        "TagOrm", secondary=task_tag_table, back_populates="tasks"
    )
