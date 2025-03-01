from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import db_helper
from app.repositories import RoomRepositories
from app.services.room_services import RoomServices


SessionDepends= Annotated[AsyncSession, Depends(db_helper.session_getter)]
async def get_room_service(
        session: SessionDepends
) -> RoomServices:
    repository = RoomRepositories(session)
    return RoomServices(repository)
