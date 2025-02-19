from app.models import RoomModel
from app.repositories import RoomRepositories
from app.schemas import RoomCreateSchema, RoomUpdateSchema


class RoomServices:

    def __init__(self, repository: RoomRepositories):
        self._repository = repository

    async def create(self, room: RoomCreateSchema) -> RoomModel:
        return await self._repository.create(room)

    async def get_one(self, room_slug: str) -> RoomModel:
        return await self._repository.get_one(room_slug)

    async def get_all(self) -> list[RoomModel]:
        return await self._repository.get_all()

    async def update(self, room: RoomModel, room_update: RoomUpdateSchema):
        return await self._repository.upgrade(
            room=room,
            room_update=room_update,
        )

    async def delete(self, room: RoomModel):
        return await self._repository.delete(room)