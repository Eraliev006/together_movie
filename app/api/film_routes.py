from typing import Annotated

from fastapi import APIRouter, Depends

from app.api.utils.film_dependencies import get_film_service, get_film_by_id
from app.models import Film
from app.schemas import FilmCreateSchema, FilmUpdateSchema
from app.services.film_service import FilmService

router = APIRouter(
    prefix='/films',
    tags=['film']
)

FilmServiceDepends = Annotated[FilmService, Depends(get_film_service)]
FilmByIdDependency = Annotated[Film, Depends(get_film_by_id)]

@router.post('/')
async def create_film(
        film: FilmCreateSchema,
        film_service: FilmServiceDepends
):
    return await film_service.create(film)

@router.get('/')
async def get_films(film_service: FilmServiceDepends):
    return await film_service.get_all()

@router.get('/{film_id}')
async def get_film(
        film_id: int,
        film_service: FilmServiceDepends
):
    return await film_service.get_by_id(film_id)

@router.put('/{film_id}')
async def update_film(
        film: FilmByIdDependency,
        film_service: FilmServiceDepends,
        film_update: FilmUpdateSchema,
):
    return await film_service.update(
        film = film,
        film_update = film_update
    )

@router.delete('/{film_id}')
async def delete_film(film: FilmByIdDependency, film_service: FilmServiceDepends):
    return await film_service.delete(film)