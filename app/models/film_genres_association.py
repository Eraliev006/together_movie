from sqlalchemy import Table, Column, ForeignKey

from app.models import Base

film_genres_association_table = Table(
    'film_genres_association',
    Base.metadata,
    Column('film_id', ForeignKey('films.id'), primary_key=True),
    Column('genre_id', ForeignKey('genres.id'), primary_key=True)
)