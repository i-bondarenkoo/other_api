from __future__ import annotations
from pydantic import BaseModel, ConfigDict

import typing

if typing.TYPE_CHECKING:
    from schemas.tag import ResponseTagSchemas
    from schemas.user import UserResponseSchemas, UserResponseWithOutRelationship


class TaskCreateSchemas(BaseModel):
    title: str
    description: str
    user_id: int


class TaskResponseSchemas(TaskCreateSchemas):
    id: int
    tags: list["ResponseTagSchemas"]
    user: "UserResponseSchemas"
    model_config = ConfigDict(from_attributes=True)


class TaskResponseSchemasWithOutRelationship(TaskCreateSchemas):
    id: int
    user: "UserResponseWithOutRelationship"
    model_config = ConfigDict(from_attributes=True)


class TaskResponseWithUser(TaskCreateSchemas):
    id: int
    user: "UserResponseWithOutRelationship"
    model_config = ConfigDict(from_attributes=True)


class FullUpdateTaskSchemas(BaseModel):
    title: str
    description: str
    user_id: int
