from pydantic import BaseModel, EmailStr, ConfigDict


class UserCreateSchemas(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr


class UserResponseSchemas(UserCreateSchemas):
    id: int

    model_config = ConfigDict(from_attributes=True)


class UpdateUserPratialSchemas(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    email: EmailStr | None = None


class UpdateUserFullSchemas(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
