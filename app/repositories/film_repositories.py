from sqlalchemy import Result, select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models import Film, FilmGenres, Actors
from app.schemas import FilmCreateSchema, FilmUpdateSchema


class FilmRepositories:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def __get_genres(self, genres_ids: list[int]) -> list[FilmGenres]:
        try:
            stmt = select(FilmGenres).where(FilmGenres.id.in_(genres_ids))
            result: Result = await self._session.execute(stmt)
            return list(result.scalars().all())
        except SQLAlchemyError as e:
            raise e

    async def __get_actors(self, actors_ids: list[int]) -> list[Actors]:
        try:
            stmt = select(Actors).where(Actors.id.in_(actors_ids))
            result: Result = await self._session.execute(stmt)
            return list(result.scalars().all())
        except SQLAlchemyError as e:
            raise e

    async def __get_film_with_genres_and_actors(self, film_id: int) -> Film | None:
        stmt = select(Film).where(Film.id == film_id).options(selectinload(Film.genres), selectinload(Film.actors))
        result: Result = await self._session.execute(stmt)
        film_with_genres = result.scalar_one_or_none()

        return film_with_genres

    async def create(self, film: FilmCreateSchema) -> Film | None:
        try:
            genres = await self.__get_genres(film.genre_ids)
            actors = await self.__get_actors(film.actor_ids)
            film_data: Film = Film(**film.model_dump(exclude={'genre_ids','actor_ids'}))
            film_data.genres = genres
            film_data.actors = actors
            self._session.add(film_data)
            await self._session.commit()
            await self._session.refresh(film_data)

            film_with_genres = await self.__get_film_with_genres_and_actors(film_data.id)
            return film_with_genres

        except SQLAlchemyError as e:
            await self._session.rollback()
            raise e

    async def get_by_id(self, film_id: int) -> Film | None:
        try:
            return await self.__get_film_with_genres_and_actors(film_id)
        except SQLAlchemyError as e:
            raise e

    async def get_all(self) -> list[Film] | None:
        try:
            stmt = select(Film).options(selectinload(Film.genres), selectinload(Film.actors))
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