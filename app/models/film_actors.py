from datetime import datetime

from sqlalchemy import Text
from sqlalchemy.orm import mapped_column, Mapped, relationship

from app.models import Base, film_actor_association_table


class Actors(Base):
    __tablename__ = 'actors'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    birthday: Mapped[datetime | None] = mapped_column(nullable=True)
    biography: Mapped[str | None] = mapped_column(Text, nullable=True)
    death_date: Mapped[datetime | None] = mapped_column(nullable=True)

    movies: Mapped[list["Movie"]] = relationship(
        secondary=film_actor_association_table,
        back_populates="actors"
    )

