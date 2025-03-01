from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import db_helper
from app.models import FilmGenres
from app.repositories import GenreRepositories
from app.services.genre_services import GenreService


def get_genre_service(
        session: AsyncSession = Depends(db_helper.session_getter)
) -> GenreService:
    repository = GenreRepositories(session)
    return GenreService(repository)

async def get_genre_by_slug(
        genre_slug: str,
        genre_service: GenreService = Depends(get_genre_service)
) -> FilmGenres:
    return await genre_service.get_by_slug(genre_slug)
