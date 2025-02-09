from datetime import datetime

from pydantic import BaseModel


class BaseFilm(BaseModel):
    title: str
    original_title: str | None
    description: str | None
    release_date: datetime | None
    duration: int | None
    rating: float | None
    poster_url: str | None
    trailer_url: str | None
    budget: int | None
    country: str | None
    age_rating: str | None

class FilmCreateSchema(BaseFilm):
    pass

class FilmOutSchemas(BaseFilm):
    id: int

class FilmUpdateSchema(BaseFilm):
    pass

