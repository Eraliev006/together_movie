from typing import Annotated

from fastapi import APIRouter, Depends

from app.api.utils import get_user_service, get_user_by_id
from app.models import UserModel
from app.schemas import UserCreateSchema, UserUpdateSchema
from app.services.user_services import UserService

router = APIRouter(
    tags=['users'],
    prefix='/users'
)

UserServiceDepends = Annotated[UserService, Depends(get_user_service)]
UserByIdDepends = Annotated[UserModel, Depends(get_user_by_id)]

@router.post('/')
async def create(user: UserCreateSchema, user_service: UserServiceDepends):
    return await user_service.create(user)


@router.get('/')
async def get_users(user_service: UserServiceDepends):
    return await user_service.get_all()

@router.get('/{user_id}')
async def get_user(user_id: int, user_service: UserServiceDepends):
    return await user_service.get_by_id(user_id)

@router.put('/{user_id}')
async def update_user(
        user_update: UserUpdateSchema,
        user_service: UserServiceDepends,
        user: UserByIdDepends
):
    return await user_service.update(user, user_update)

@router.delete('/{user_id}')
async def delete_user(
        user_service: UserServiceDepends,
        user: UserByIdDepends
):
    return await user_service.delete(user)