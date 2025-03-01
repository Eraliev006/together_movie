from sqlalchemy import select, Result
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import RoomModel
from app.schemas import RoomUpdateSchema, RoomCreateSchema


class RoomRepositories:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create(self, room: RoomCreateSchema) -> RoomModel | None:
        try:
            room = RoomModel(**room.model_dump())
            self._session.add(room)
            await self._session.commit()
            await self._session.refresh(room)
            return room
        except SQLAlchemyError as e:
            await self._session.rollback()
            raise e

    async def get_one(self, room_slug: str) -> RoomModel | None:
        try:
            stmt = select(RoomModel).where(RoomModel.slug == room_slug)
            result: Result = await self._session.execute(stmt)
            return result.scalar_one_or_none()
        except SQLAlchemyError as e:
            raise e

    async def get_all(self) -> list[RoomModel] | None:
        try:
            stmt = select(RoomModel)
            result: Result = await self._session.execute(stmt)

            return list(result.scalars().all())

        except SQLAlchemyError as e:
            raise e

    async def upgrade(self, room: RoomModel, room_update: RoomUpdateSchema) -> RoomModel | None:
        try:
            for key, value in room_update.model_dump(exclude_unset=True).items():
                setattr(room, key, value)
            await self._session.commit()
            return room
        except SQLAlchemyError as e:
            await self._session.rollback()
            raise e

    async def delete(self, room: RoomModel) -> None:
        try:
            await self._session.delete(room)
            await self._session.commit()
        except SQLAlchemyError as e:
            await self._session.rollback()
            raise e

    async def get_room_by_name(self, name: str) -> RoomModel | None:
        try:
            stmt = select(RoomModel).where(RoomModel.name == name)
            result: Result = await self._session.execute(stmt)
            return result.scalar_one_or_none()
        except SQLAlchemyError as e:
            raise e