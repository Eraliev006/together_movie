
from pydantic import BaseModel

class GenreCreateSchemas(BaseModel):
    name: str

class GenreAddToDB(GenreCreateSchemas):
    slug: str

class GenreOutSchemas(GenreCreateSchemas):
    id: int
    slug: str

class GenreUpdateSchemas(GenreCreateSchemas):
    pass