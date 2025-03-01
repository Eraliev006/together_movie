from typing import Annotated

from fastapi import APIRouter, Depends

from app.api.utils import get_actor_service, get_actor_by_id
from app.models import Actors
from app.schemas import CreateActorSchemas, UpdateActorSchemas
from app.services.actor_services import ActorServices

router = APIRouter(
    tags=['actors'],
    prefix='/actors'
)

ActorServiceDepends = Annotated[ActorServices, Depends(get_actor_service)]
ActorByIdDepends = Annotated[Actors, Depends(get_actor_by_id)]

@router.get('/')
async def get_all(
        service: ActorServiceDepends
):
    return await service.get_all()

@router.post('/')
async def create_actor(
        actor: CreateActorSchemas,
        service: ActorServiceDepends
):
    return await service.create(actor)

@router.get('/{actor_id}')
async def get_by_id(
        service: ActorServiceDepends,
        actor_id: int):
    return service.get_by_id(actor_id)

@router.put('/{actor_id}')
async def update_actor(
        actor_update: UpdateActorSchemas,
        actor: ActorByIdDepends,
        service: ActorServiceDepends,
):
    return service.update(actor, actor_update)

@router.delete('/{actor_id}')
async def delete_actor(service: ActorServiceDepends, actor: ActorByIdDepends):
    return service.delete(actor)