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

class UserUpdateSchema(BaseUser):
    pass