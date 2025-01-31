from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Base


class RoomModel(Base):
    __tablename__ = 'rooms'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    name: Mapped[str] = mapped_column(String(50), unique=True)

    host_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'), nullable=False)

    users: Mapped[list['UserModel']] = relationship(back_populates='room')