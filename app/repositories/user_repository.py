from sqlalchemy import Result, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError

from app.models import UserModel
from app.schemas import UserAddToDB, UserCreateSchema
from app.schemas.user_schemas import UserUpdateSchema


class UserRepository:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def create(self, user: UserAddToDB):
        try:
            user: UserModel = UserModel(**user.model_dump())
            self._session.add(user)
            await self._session.commit()
            await self._session.refresh(user)
            return user
        except SQLAlchemyError as e:
            await self._session.rollback()
            raise e
    
    async def get_by_id(self, user_id: int):
        try:
            return await self._session.get(UserModel, user_id)
        except SQLAlchemyError as e:
            raise e
        
    async def get_all(self):
        try:
            stmt = select(UserModel)
            result: Result = await self._session.execute(stmt)
            return result.scalars().all()
        
        except SQLAlchemyError as e:
            raise e
        
    async def update(self, user:UserModel, user_update: UserUpdateSchema):
        try:
            for name, value in user_update.model_dump(exclude_unset=True).items():
                setattr(user, name, value)
            await self._session.commit()
            return user
        except SQLAlchemyError as e:
            await self._session.rollback()
            raise e
        
    async def delete(self, user: UserModel):
        try:
            await self._session.delete(user)
            await self._session.commit()
        except SQLAlchemyError as e:
            await self._session.rollback()
            raise e