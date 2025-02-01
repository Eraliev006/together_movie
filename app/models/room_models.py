from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Base, UserModel


class RoomModel(Base):
    __tablename__ = 'rooms'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    name: Mapped[str] = mapped_column(String(50), unique=True)
    host_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    slug: Mapped[str] = mapped_column(nullable=False, unique=True)

    users: Mapped[list['UserModel']] = relationship( back_populates='room', foreign_keys=[UserModel.current_room_id])
    host: Mapped['UserModel'] = relationship(foreign_keys=[host_id])