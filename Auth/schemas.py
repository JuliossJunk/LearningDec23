import uuid
from typing import Optional

from fastapi_users import schemas
from fastapi_users.schemas import PYDANTIC_V2


class UserRead(schemas.BaseUser[uuid.UUID]):
    id: int
    email: str
    username: str
    role_id: int
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    if PYDANTIC_V2:  # pragma: no cover
        model_config = ConfigDict(from_attributes=True)  # type: ignore
    else:  # pragma: no cover

        class Config:
            orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    username: str
    email: str
    password: str
    role_id: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False

# for updating user information
# class UserUpdate(schemas.BaseUserUpdate):
#     username: Optional[str] = None
#     password: Optional[str] = None
#     email: Optional[str] = None
#     role_id: Optional[str] = None
#     is_active: Optional[bool] = None
#     is_superuser: Optional[bool] = None
#     is_verified: Optional[bool] = None
