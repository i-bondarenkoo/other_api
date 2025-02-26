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
    # "ResponseTagWithUserAndTask",
    "ResponseTagWithOutRelationship",
)
from schemas.tag import (
    CreateTagSchemas,
    ResponseTagSchemas,
    FullUpdateTagSchemas,
    # ResponseTagWithUserAndTask,
    ResponseTagWithOutRelationship,
)
from schemas.task import (
    TaskCreateSchemas,
    TaskResponseSchemas,
    FullUpdateTaskSchemas,
    TaskResponseSchemasWithOutRelationship,
)
from schemas.user import (
    UpdateUserPartialSchemas,
    UserCreateSchemas,
    UserResponseSchemas,
    UpdateUserFullSchemas,
    UserResponseWithOutRelationship,
)

UserResponseSchemas.model_rebuild()
# ResponseTagWithUserAndTask.model_rebuild()
ResponseTagWithOutRelationship.model_rebuild()
