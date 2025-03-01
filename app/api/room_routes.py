from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Depends
from starlette.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_204_NO_CONTENT

from app.api.utils import get_room_service
from app.schemas import RoomCreateSchema, RoomOutSchema
from app.services.room_services import RoomServices

router = APIRouter(
    prefix='/rooms',
    tags=['room']
)

RoomServiceDepends = Annotated[RoomServices, Depends(get_room_service)]

@router.post('/', status_code=HTTP_201_CREATED, response_model=RoomOutSchema)
async def create_room(
        room: RoomCreateSchema,
        room_service: RoomServiceDepends
):
    return await room_service.create(room)

@router.get('/', status_code=HTTP_200_OK, response_model=list[RoomOutSchema])
async def get_all_room(room_service: RoomServiceDepends):
    return await room_service.get_all()

@router.get('/{room_slug}', status_code=HTTP_200_OK, response_model=RoomOutSchema)
async def get_one(room_slug:str, room_service: RoomServiceDepends):
    return await room_service.get_one(room_slug)

@router.delete('/{room_slug}', status_code=HTTP_204_NO_CONTENT, response_model = None)
async def delete(
        room_service: RoomServiceDepends,
        room_slug: str
):
    return await room_service.delete(room_slug)