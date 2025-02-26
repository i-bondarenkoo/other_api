from pydantic import BaseModel, ConfigDict
import typing

if typing.TYPE_CHECKING:
    from schemas.task import TaskResponseSchemas


class CreateTagSchemas(BaseModel):
    name: str


class ResponseTagSchemas(BaseModel):
    id: int
    name: str
    tasks: list["TaskResponseSchemas"]
    model_config = ConfigDict(from_attributes=True)


class ResponseTagWithUserAndTask(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)


class ResponseTagWithOutRelationship(CreateTagSchemas):
    id: int
    model_config = ConfigDict(from_attributes=True)


class FullUpdateTagSchemas(BaseModel):
    name: str
