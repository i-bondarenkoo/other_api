__all__ = (
    "UpdateUserPartialSchemas",
    "UserCreateSchemas",
    "UserResponseSchemas",
    "UpdateUserFullSchemas",
    "TaskCreateSchemas",
    "TaskResponseSchemas",
    "FullUpdateTaskSchemas",
    "CreateTagSchemas",
    "ResponseTagSchemas",
    "UserResponseWithOutRelationship",
    "FullUpdateTagSchemas",
    "TaskResponseSchemasWithOutRelationship",
    "ResponseTagWithUserAndTask",
    "TaskResponseWithUser",
)
from schemas.tag import (
    CreateTagSchemas,
    ResponseTagSchemas,
    FullUpdateTagSchemas,
    ResponseTagWithUserAndTask,
)
from schemas.task import (
    TaskCreateSchemas,
    TaskResponseSchemas,
    FullUpdateTaskSchemas,
    TaskResponseSchemasWithOutRelationship,
    TaskResponseWithUser,
)
from schemas.user import (
    UpdateUserPartialSchemas,
    UserCreateSchemas,
    UserResponseSchemas,
    UpdateUserFullSchemas,
    UserResponseWithOutRelationship,
)

UserResponseSchemas.model_rebuild()
ResponseTagWithUserAndTask.model_rebuild()
TaskResponseWithUser.model_rebuild()
