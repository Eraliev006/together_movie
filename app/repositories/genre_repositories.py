from sqlalchemy import select, Result
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import FilmGenres
from app.schemas import GenreUpdateSchemas, GenreAddToDB


class GenreRepositories:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def create(self, genre: GenreAddToDB) -> FilmGenres:
        try:
            genre: FilmGenres = FilmGenres(**genre.model_dump())
            self._session.add(genre)
            await self._session.commit()
            await self._session.refresh(genre)
            return genre
        except SQLAlchemyError as e:
            await self._session.rollback()
            raise e

    async def get_by_slug(self, genre_slug: str) -> FilmGenres | None:
        try:
            stmt = select(FilmGenres).where(FilmGenres.slug == genre_slug)
            result: Result = await self._session.execute(stmt)
            return result.scalar_one_or_none()
        except SQLAlchemyError as e:
            raise e

    async def get_all(self) -> list[FilmGenres] | None:
        try:
            stmt = select(FilmGenres)
            result: Result = await self._session.execute(stmt)
            return list(result.scalars().all())

        except SQLAlchemyError as e:
            raise e

    async def update(self, genre: FilmGenres, genre_update: GenreAddToDB) -> FilmGenres | None:
        try:
            for name, value in genre_update.model_dump(exclude_unset=True).items():
                setattr(genre, name, value)
            await self._session.commit()
            return genre
        except SQLAlchemyError as e:
            await self._session.rollback()
            raise e

    async def delete(self, genre: FilmGenres):
        try:
            await self._session.delete(genre)
            await self._session.commit()
        except SQLAlchemyError as e:
            await self._session.rollback()
            raise e