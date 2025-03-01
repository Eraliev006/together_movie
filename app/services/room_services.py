from app.exceptions import RoomAlreadyExists, RoomNotFoundException
from app.models import RoomModel
from app.repositories import RoomRepositories
from app.schemas import RoomCreateSchema, RoomUpdateSchema, RoomOutSchema
from app.services.utils import generate_slug


class RoomServices:

    def __init__(self, repository: RoomRepositories):
        self._repository = repository

    async def __is_room_with_name_already_exists(self, name: str) -> bool:
        room = await self._repository.get_room_by_name(name)
        return True if room else False

    @staticmethod
    def __convert_sqlmodel_to_room_out_schemas(room: RoomModel) -> RoomOutSchema:
        return RoomOutSchema(
            id = room.id,
            name = room.name,
            slug = room.slug,
            host_id = room.host_id
        )

    async def create(self, room: RoomCreateSchema) -> RoomOutSchema:
        if await self.__is_room_with_name_already_exists(room.name):
            raise RoomAlreadyExists(f'Room with name {room.name} already exists, change name')

        slug: str = generate_slug(room.name)
        created: RoomModel = await self._repository.create(room, slug)
        return self.__convert_sqlmodel_to_room_out_schemas(created)

    async def get_one(self, room_slug: str) -> RoomOutSchema:
        room: RoomModel | None = await self._repository.get_one(room_slug)
        if not room:
            raise RoomNotFoundException(f'Room with slug-{room_slug} not found')
        return self.__convert_sqlmodel_to_room_out_schemas(room)

    async def get_all(self) -> list[RoomOutSchema]:
        return [self.__convert_sqlmodel_to_room_out_schemas(i) for i in await self._repository.get_all()]

    async def update(self, room_slug: str, room_update: RoomUpdateSchema) -> RoomOutSchema:
        room: RoomModel | None = await self._repository.get_one(room_slug)
        if not room:
            raise RoomNotFoundException(f'Room with slug-{room_slug} not found')
        upgraded: RoomModel = await self._repository.upgrade(
            room=room,
            room_update=room_update,
        )
        return self.__convert_sqlmodel_to_room_out_schemas(upgraded)

    async def delete(self, room_slug: str) -> None:
        room: RoomModel | None = await self._repository.get_one(room_slug)
        if not room:
            raise RoomNotFoundException(f'Room with slug-{room_slug} not found')
        return await self._repository.delete(room)