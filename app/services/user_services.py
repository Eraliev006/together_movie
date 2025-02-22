import bcrypt

from app.exceptions import UserAlreadyExistsException, UserNotFoundException
from app.models import UserModel
from app.repositories.user_repository import UserRepository
from app.schemas import UserCreateSchema, UserAddToDB, UserOutSchema
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

    @staticmethod
    def __convert_from_sqlmodel_to_pydantic(user: UserModel) -> UserOutSchema | None:
        return UserOutSchema(
            id = user.id,
            username = user.username,
            email = user.email,
            is_active = user.is_active
        )

    async def create(self, user: UserCreateSchema) -> UserOutSchema | None:
        exists_user = await self.get_user_by_email_or_username(user.email, user.username)
        if exists_user:
            raise UserAlreadyExistsException(f'User with {user.email}-email  or {user.username}-usernname already exists')

        hashed_pwd = self.__hash_password(user.password)
        user = UserAddToDB(
            **user.model_dump(exclude={'password'}),
            password = hashed_pwd
        )
        created_user: UserModel = await self._repository.create(user)
        return self.__convert_from_sqlmodel_to_pydantic(created_user)

    async def get_all(self) -> list[UserOutSchema]:
        result: list[UserModel] = await self._repository.get_all()
        return [self.__convert_from_sqlmodel_to_pydantic(user) for user in result]

    async def get_by_id(self, user_id: int) -> UserOutSchema:
        user = await self._repository.get_by_id(user_id)
        if not user:
            raise UserNotFoundException(f'User with ID-{user_id} not found')

        return self.__convert_from_sqlmodel_to_pydantic(user)

    async def update(self, user_id: int, update_user: UserUpdateSchema) -> UserOutSchema:
        user = await self._repository.get_by_id(user_id)

        exists_user = await self.get_user_by_email_or_username(update_user.email, update_user.username)
        if exists_user:
            raise UserAlreadyExistsException(f'User with {user.email}-email  or {user.username}-usernname already exists')

        result: UserModel = await self._repository.update(
            user = user,
            user_update = update_user
        )
        return self.__convert_from_sqlmodel_to_pydantic(result)

    async def delete(self, user_id: int):
        user = await self._repository.get_by_id(user_id)
        if user:
            return await self._repository.delete(user)
        raise UserNotFoundException(f'User with ID-{user_id} not found')

    async def get_user_by_email_or_username(self, email: str | None, username: str | None) -> UserOutSchema | None:
        result: UserModel = await self._repository.get_user_by_email_or_username(email,username)
        if result:
            return self.__convert_from_sqlmodel_to_pydantic(result)
        return None