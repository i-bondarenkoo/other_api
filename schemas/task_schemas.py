from pydantic import BaseModel, ConfigDict


class TaskCreateSchemas(BaseModel):
    title: str
    description: str
    user_id: int


class TaskResponseSchemas(TaskCreateSchemas):
    id: int

    model_config = ConfigDict(from_attributes=True)


class FullUpdateTaskSchemas(BaseModel):
    title: str
    description: str
    user_id: int
