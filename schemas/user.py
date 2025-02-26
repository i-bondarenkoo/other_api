from __future__ import annotations
from pydantic import BaseModel, EmailStr, ConfigDict

import typing

if typing.TYPE_CHECKING:
    from schemas.task import TaskResponseSchemas


class UserCreateSchemas(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr


class UserResponseSchemas(UserCreateSchemas):
    id: int
    tasks: list["TaskResponseSchemas"]
    model_config = ConfigDict(from_attributes=True)


class UserResponseWithOutRelationship(UserCreateSchemas):
    id: int
    model_config = ConfigDict(from_attributes=True)


class UpdateUserPartialSchemas(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    email: EmailStr | None = None


class UpdateUserFullSchemas(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
