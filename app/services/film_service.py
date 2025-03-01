from app.models import Film
from app.repositories import FilmRepositories
from app.schemas import FilmCreateSchema, FilmUpdateSchema


class FilmService:
    def __init__(self, repository: FilmRepositories):
        self._repository: FilmRepositories = repository

    async def create(self, film: FilmCreateSchema) -> Film | None:
        return await self._repository.create(film)

    async def get_by_id(self, film_id: int) -> Film | None:
        return await self._repository.get_by_id(film_id)

    async def get_all(self) -> list[Film] | None:
        return await self._repository.get_all()

    async def update(self, film: Film, film_update: FilmUpdateSchema) -> Film | None:
        return await self._repository.update(
            film, film_update
        )

    async def delete(self, film: Film) -> None:
        return await self._repository.delete(film)


