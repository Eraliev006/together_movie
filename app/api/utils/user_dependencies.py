from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import db_helper
from app.repositories import UserRepository
from app.schemas import UserOutSchema
from app.services.user_services import UserService


def get_user_service(
        session: AsyncSession = Depends(db_helper.session_getter)
) -> UserService:
    repository = UserRepository(session)
    return UserService(repository)
