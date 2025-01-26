from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import db_helper
from app.repositories.user_repository import UserRepository
from app.schemas import UserCreateSchema, UserUpdateSchema
from app.services.user_services import UserService

router = APIRouter(
    tags=['users'],
    prefix='/users'
)

def get_user_service(
        session: AsyncSession = Depends(db_helper.session_getter)
) -> UserService:
    repository = UserRepository(session)
    return UserService(repository)

@router.post('/')
async def create(user: UserCreateSchema, user_service: UserService = Depends(get_user_service)):
    return await user_service.create(user)


@router.get('/')
async def get_all_users(user_service: UserService = Depends(get_user_service)):
    return await user_service.get_all()

@router.get('/{user_id}')
async def get_user_by_id(user_id: int, user_service: UserService = Depends(get_user_service)):
    return await user_service.get_by_id(user_id)

# @router.put('/{user_id}')
# async def update_user(
#         user_id: int, user_update: UserUpdateSchema,
#         user_service: UserService = Depends(get_user_service)
#                       ):
#     return await user_service.update()