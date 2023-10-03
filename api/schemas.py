from pydantic import BaseModel, field_validator


class CreateUserRequestSchema(BaseModel):
    username: str
    password: str


class CreateUserResponseSchema(BaseModel):
    id: int
    username: str


class DeleteUserRequestSchema(BaseModel):
    password: str
