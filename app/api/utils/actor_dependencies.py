from typing import Annotated

from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import db_helper
from app.repositories import ActorRepositories
from app.services.actor_services import ActorServices


def get_actor_service(session: AsyncSession =  Depends(db_helper.session_getter)) -> ActorServices:
    repository = ActorRepositories(session)
    return ActorServices(repository)

async def get_actor_by_id(
        service: Annotated[ActorServices,Depends(get_actor_service)],
        actor_id: int
):
    return await service.get_by_id(actor_id)