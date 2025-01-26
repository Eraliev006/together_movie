from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import db_helper
from app.models import UserModel
from app.repositories import UserRepository
from app.services.user_services import UserService


def get_user_service(
        session: AsyncSession = Depends(db_helper.session_getter)
) -> UserService:
    repository = UserRepository(session)
    return UserService(repository)

async def get_user_by_id(
        user_id: int,
        user_service: UserService = Depends(get_user_service)
) -> UserModel:
    return await user_service.get_by_id(user_id)
