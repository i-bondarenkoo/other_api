from pydantic import BaseModel, ConfigDict


class CreateTagSchemas(BaseModel):
    name: str


class ResponseTagSchemas(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)


class FullUpdateTagSchemas(BaseModel):
    name: str
