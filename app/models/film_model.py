from sqlalchemy import String, Text, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Base, film_actor_association_table

class Film(Base):
    __tablename__ = 'films'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    original_title: Mapped[str | None] = mapped_column(String(255), nullable=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    release_date: Mapped[Date | None] = mapped_column(Date, nullable=True)
    duration: Mapped[int | None] = mapped_column(nullable=True)
    rating: Mapped[float | None] = mapped_column(nullable=True)
    poster_url: Mapped[str | None] = mapped_column(nullable=True)
    trailer_url: Mapped[str | None] = mapped_column(nullable=True)
    budget: Mapped[int | None] = mapped_column(nullable=True)
    country: Mapped[str | None] = mapped_column(String(100), nullable=True)
    age_rating: Mapped[str | None] = mapped_column(String(10), nullable=True)

    genres: Mapped[list['FilmGenres']] = relationship(
        secondary='film_genres_association', back_populates="films"
    )
    actors: Mapped[list["Actors"]] = relationship(
        secondary=film_actor_association_table,
        back_populates="movies"
    )