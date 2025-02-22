from typing import Annotated

from fastapi import APIRouter, Depends
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_202_ACCEPTED, HTTP_204_NO_CONTENT

from app.api.utils import get_user_service
from app.schemas import UserCreateSchema, UserUpdateSchema, UserOutSchema
from app.services.user_services import UserService

router = APIRouter(
    tags=['users'],
    prefix='/users'
)

UserServiceDepends = Annotated[UserService, Depends(get_user_service)]

@router.post('/', response_model=UserOutSchema, status_code=201)
async def create(user: UserCreateSchema, user_service: UserServiceDepends):
    return await user_service.create(user)


@router.get('/',
                response_model = list[UserOutSchema],
                status_code = HTTP_201_CREATED)
async def get_users(user_service: UserServiceDepends):
    return await user_service.get_all()

@router.get('/{user_id}',
            response_model=UserOutSchema,
            status_code=HTTP_200_OK)
async def get_user(user_id: int, user_service: UserServiceDepends):
    return await user_service.get_by_id(user_id)

@router.put('/{user_id}', response_model=UserOutSchema,
            status_code=HTTP_202_ACCEPTED)
async def update_user(
        user_update: UserUpdateSchema,
        user_service: UserServiceDepends,
        user_id: int
):
    return await user_service.update(user_id, user_update)

@router.delete('/{user_id}',
            status_code=HTTP_204_NO_CONTENT, response_model=None)
async def delete_user(
        user_service: UserServiceDepends,
        user_id: int
):
    return await user_service.delete(user_id)