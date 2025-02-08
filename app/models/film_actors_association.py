from sqlalchemy import Table, Column, ForeignKey

from app.models import Base

film_actor_association_table = Table(
    'film_actor_association',
    Base.metadata,
    Column("film_id", ForeignKey('films.id'), primary_key=True),
    Column("actor_id", ForeignKey('actors.id'), primary_key=True)
)