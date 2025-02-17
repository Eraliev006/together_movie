from fastapi import APIRouter

from .user_routes import router as user_router
from .room_routes import router as room_router
from .film_routes import router as film_router
from .genre_routes import router as genre_router
from .actor_routes import router as actor_router
from ..core import settings

router = APIRouter(
    prefix=settings.api_prefix
)

router.include_router(user_router)
router.include_router(room_router)
router.include_router(film_router)
router.include_router(genre_router)
router.include_router(actor_router)