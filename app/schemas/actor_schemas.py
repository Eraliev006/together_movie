from datetime import datetime

from pydantic import BaseModel


class BaseActor(BaseModel):
    name: str
    birthday: datetime | None
    biography: str | None
    death_date: datetime | None


class CreateActorSchemas(BaseActor):
    pass

class UpdateActorSchemas(BaseActor):
    pass


