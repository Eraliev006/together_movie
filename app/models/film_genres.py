from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Base
from .film_genres_association import film_genres_association_table



class FilmGenres(Base):
    __tablename__ = '__tablename__genres'

    id: Mapped[int] = mapped_column(nullable=False, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    slug: Mapped[str] = mapped_column(nullable=False)

    films: Mapped[list['Film']] = relationship(
        secondary=film_genres_association_table, back_populates="genres"
    )
