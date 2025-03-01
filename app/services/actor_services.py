from app.models import Actors
from app.repositories import ActorRepositories
from app.schemas import CreateActorSchemas, UpdateActorSchemas


class ActorServices:
    def __init__(self, repository: ActorRepositories):
        self._repository = repository

    async def create(self, actor: CreateActorSchemas) -> Actors | None:
        return await self._repository.create(actor)

    async def get_all(self) -> list[Actors] | None:
        return await self._repository.get_all()

    async def get_by_id(self, actor_id: int) -> Actors | None:
        return await self._repository.get_by_id(actor_id)

    async def update(self, actor: Actors, update_actor: UpdateActorSchemas) -> Actors | None:
        return await self._repository.update(actor, update_actor)

    async def delete(self, actor: Actors) -> None:
        return await self._repository.delete(actor)