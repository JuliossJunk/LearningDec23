import uuid
from typing import Optional

from fastapi_users import schemas
from fastapi_users.schemas import PYDANTIC_V2


class UserRead(schemas.BaseUser[int]):
    id: int
    email: str
    username: str
    role_id: int
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        from_attributes = True


class UserCreate(schemas.BaseUserCreate):
    username: str
    email: str
    password: str
    role_id: int
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False

# for updating user information
class UserUpdate(schemas.BaseUserUpdate):
    username: Optional[str] = None
    password: Optional[str] = None
    email: Optional[str] = None
    role_id: Optional[str] = None
    is_active: Optional[bool] = None
    is_superuser: Optional[bool] = None
    is_verified: Optional[bool] = None
