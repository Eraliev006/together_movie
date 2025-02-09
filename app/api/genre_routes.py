from typing import Annotated

from fastapi import APIRouter, Depends

from app.api.utils import get_genre_service, get_genre_by_slug
from app.models import FilmGenres
from app.schemas import GenreCreateSchemas, GenreUpdateSchemas
from app.services.genre_services import GenreService

router = APIRouter(
    tags=['genre'],
    prefix='/genres'
)

GenreServiceDepends = Annotated[GenreService, Depends(get_genre_service)]
GenreBySlugDepends = Annotated[FilmGenres, Depends(get_genre_by_slug)]

@router.post('/')
async def create_genres(
        genre_service: GenreServiceDepends,
        genre: GenreCreateSchemas,
):
    return await genre_service.create(genre)

@router.get('/{genre_slug}')
async def get_genres_by_slug(
        genre_slug: str,
        genre_service: GenreServiceDepends,
):
    return await genre_service.get_by_slug(genre_slug)

@router.get('/')
async def get_genres(
    genre_service: GenreServiceDepends
):
    return await genre_service.get_all()

@router.put('/{genre_slug}')
async def update_genres(
        genre_service: GenreServiceDepends,
        genre_update: GenreUpdateSchemas,
        genre: GenreBySlugDepends
):
    return await genre_service.update(genre, genre_update)

@router.delete('/{genre_slug}')
async def delete_genre(
        genre: GenreBySlugDepends,
        genre_service: GenreServiceDepends,
):
    return await genre_service.delete(genre)