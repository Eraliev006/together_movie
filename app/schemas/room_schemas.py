from pydantic import BaseModel


class RoomCreateSchema(BaseModel):
    name: str
    host_id: int

class RoomOutSchema(RoomCreateSchema):
    id: int

class RoomUpdateSchema(BaseModel):
    name: str