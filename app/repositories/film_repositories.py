from sqlalchemy import Result, select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Film
from app.schemas import FilmCreateSchema, FilmUpdateSchema


class FilmRepositories:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def create(self, film: FilmCreateSchema) -> Film:
        try:
            film: Film = Film(**film.model_dump())
            self._session.add(film)
            await self._session.commit()
            await self._session.refresh(film)
            return film
        except SQLAlchemyError as e:
            await self._session.rollback()
            raise e

    async def get_by_id(self, film_id: int) -> Film | None:
        try:
            return await self._session.get(Film, film_id)
        except SQLAlchemyError as e:
            raise e

    async def get_all(self) -> list[Film] | None:
        try:
            stmt = select(Film)
            result: Result = await self._session.execute(stmt)
            return list(result.scalars().all())

        except SQLAlchemyError as e:
            raise e

    async def update(self, film: Film, film_update: FilmUpdateSchema) -> Film | None:
        try:
            for name, value in film_update.model_dump(exclude_unset=True).items():
                setattr(film, name, value)
            await self._session.commit()
            return film
        except SQLAlchemyError as e:
            await self._session.rollback()
            raise e

    async def delete(self, film: Film):
        try:
            await self._session.delete(film)
            await self._session.commit()
        except SQLAlchemyError as e:
            await self._session.rollback()
            raise e