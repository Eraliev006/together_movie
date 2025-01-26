from fastapi import APIRouter

from .user_routes import router as user_router
from ..core import settings

router = APIRouter(
    prefix=settings.api_prefix
)

router.include_router(user_router)