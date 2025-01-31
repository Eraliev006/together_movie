
from sqlalchemy import String, ForeignKey
from app.models import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship


class UserModel(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    username: Mapped[str] = mapped_column(String(80), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[bytes] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True, nullable=False)
    current_room_id: Mapped[int] = mapped_column(ForeignKey("rooms.id", ondelete='SET NULL'), nullable=True)

    room: Mapped['RoomModel'] = relationship(back_populates='users', foreign_keys=[current_room_id])

