from slugify import slugify

from app.models import FilmGenres
from app.repositories import GenreRepositories
from app.schemas import GenreCreateSchemas, GenreUpdateSchemas
from app.schemas.genre_schemas import GenreAddToDB


class GenreService:
    def __init__(self, repository: GenreRepositories):
        self._repository = repository

    @staticmethod
    def __generate_slug(name: str) -> str:
        return slugify(name, separator='-')

    def __convert_to_add_to_db_schemas(self, genre: GenreCreateSchemas) -> GenreAddToDB:
        genre_name = genre.name
        genre = GenreAddToDB(name = genre_name, slug = self.__generate_slug(genre_name))
        return genre

    async def create(self, genre: GenreCreateSchemas) -> FilmGenres | None:
        genre = self.__convert_to_add_to_db_schemas(genre)
        return await self._repository.create(genre)

    async def get_by_slug(self, genre_slug: str) -> FilmGenres | None:
        return await self._repository.get_by_slug(genre_slug)

    async def get_all(self) -> list[FilmGenres] | None:
        return await self._repository.get_all()

    async def update(self, genre: FilmGenres, genre_update: GenreUpdateSchemas):
        genre_update = self.__convert_to_add_to_db_schemas(genre_update)
        return await self._repository.update(genre, genre_update)

    async def delete(self, genre: FilmGenres) -> None:
        return await self._repository.delete(genre)