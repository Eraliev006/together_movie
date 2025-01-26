from typing import Optional

from pydantic import BaseModel, EmailStr


class BaseUser(BaseModel):
    username: str
    email: EmailStr
    is_active: bool = True

class UserCreateSchema(BaseUser):
    password: str

class UserOutSchema(BaseUser):
    id: int

class UserAddToDB(BaseUser):
    password: bytes

class UserUpdateSchema(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True