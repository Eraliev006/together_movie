from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Depends

from app.api.utils import get_room_service, get_room_by_id
from app.models import RoomModel
from app.schemas import RoomCreateSchema
from app.services.room_services import RoomServices

router = APIRouter(
    prefix='/room',
    tags=['room']
)

RoomServiceDepends = Annotated[RoomServices, Depends(get_room_service)]

@router.post('/')
async def create_room(
        room: RoomCreateSchema,
        room_service: RoomServiceDepends
):
    return await room_service.create(room)

@router.get('/')
async def get_all_room(room_service: RoomServiceDepends):
    return await room_service.get_all()

@router.get('/{room_id}')
async def get_by_id(room_id:int, room_service: RoomServiceDepends):
    return await room_service.get_by_id(room_id)

@router.delete('/{room_id}')
async def delete(
        room: RoomModel = Depends(get_room_by_id),
        room_service: RoomServices = Depends(RoomServiceDepends)
):
    return await room_service.delete(room)