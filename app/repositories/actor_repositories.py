from sqlalchemy import select, Result
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models import Actors
from app.schemas import CreateActorSchemas, UpdateActorSchemas


class ActorRepositories:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def create(self, actor: CreateActorSchemas) -> Actors | None:
        try:
            actor_data = Actors(**actor.model_dump())
            self._session.add(actor_data)
            await self._session.commit()
            await self._session.refresh(actor_data)
            return actor_data
        except SQLAlchemyError as e:
            await self._session.rollback()
            raise e

    async def get_all(self) -> list[Actors] | None:
        try:
            stmt = select(Actors).options(selectinload(Actors.movies))
            result: Result = await self._session.execute(stmt)
            return list(result.scalars().all())
        except SQLAlchemyError as e:
            raise e

    async def get_by_id(self, actor_id: int) -> Actors | None:
        try:
            stmt = select(Actors).where(Actors.id == actor_id).options(
                selectinload(Actors.movies)
            )
            result: Result = await self._session.execute(stmt)
            return result.scalar_one_or_none()
        except SQLAlchemyError as e:
            raise e

    async def update(self, actor: Actors, update_actor: UpdateActorSchemas):
        try:
            for name, value in update_actor.model_dump(exclude_unset=True).items():
                setattr(actor, name, value)
            await self._session.commit()
            return actor
        except SQLAlchemyError as e:
            await self._session.rollback()
            raise e

    async def delete(self, actor: Actors):
        try:
            await self._session.delete(actor)
            await self._session.commit()
        except SQLAlchemyError as e:
            await self._session.rollback()
            raise e