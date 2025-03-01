from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import db_helper
from app.models import Film
from app.repositories import FilmRepositories
from app.services.film_service import FilmService


def get_film_service(
        session: AsyncSession = Depends(db_helper.session_getter)
) -> FilmService:
    repository = FilmRepositories(session)
    return FilmService(repository)

async def get_film_by_id(
        film_id: int,
        film_service: FilmService = Depends(get_film_service)
) -> Film:
    return await film_service.get_by_id(film_id)
