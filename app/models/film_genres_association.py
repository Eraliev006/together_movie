from sqlalchemy import UniqueConstraint, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.models import Base

class FilmGenreAssociation(Base):
    __tablename__ = 'film_genres_association'
    __table_args__ = (
        UniqueConstraint('film_id', 'genre_id', name='idx_unique_film_genre'),
    )

    film_id: Mapped[int] = mapped_column(ForeignKey('genres.id'), primary_key=True, nullable=False)
    genre_id: Mapped[int] = mapped_column(ForeignKey('films.id'),primary_key=True, nullable=False)
