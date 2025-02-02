from sqlalchemy import Date, Text
from sqlalchemy.orm import mapped_column, Mapped

from app.models import Base


class Actors(Base):
    __tablename__ = 'actors'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    birthday: Mapped[Date | None] = mapped_column(nullable=True)
    biography: Mapped[str | None] = mapped_column(Text, nullable=True)
    death_date: Mapped[Date | None] = mapped_column(nullable=True)

