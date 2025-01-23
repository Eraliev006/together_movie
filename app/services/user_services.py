import bcrypt
from watchfiles import awatch

from app.models import UserModel
from app.repositories.user_repository import UserRepository
from app.schemas import UserCreateSchema, UserAddToDB
from app.schemas.user_schemas import UserUpdateSchema


class UserService:
    def __init__(self, repository: UserRepository):
        self._repository = repository

    @staticmethod
    def __hash_password(password: str) -> bytes:
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(
            password.encode(),
            salt
        )

    async def create(self, user: UserCreateSchema) -> UserModel | None:
        hashed_pwd = self.__hash_password(user.password)
        user = UserAddToDB(
            **user.model_dump(exclude={'password'}),
            pasword = hashed_pwd
        )
        return await self._repository.create(user)

    async def get_all(self):
        return await self._repository.get_all()

    async def get_by_id(self, user_id: int) -> UserModel:
        return await self._repository.get_by_id(user_id)

    async def update(self, user: UserModel, update_user: UserUpdateSchema):
        return await self._repository.update(
            user = user,
            user_update = update_user
        )

    async def delete(self, user: UserModel):
        return await self._repository.delete(user)
