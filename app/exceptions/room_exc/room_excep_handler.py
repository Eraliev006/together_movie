from starlette.requests import Request
from starlette.responses import JSONResponse

from app.exceptions.room_exc import RoomNotFoundException, RoomAlreadyExists


async def room_not_found_exception_handler(request: Request, exc: RoomNotFoundException):
    return JSONResponse(
        status_code=404,
        content={'message': f'{exc.message}'}
    )

async def room_already_exists_exception_handler(request: Request, exc: RoomAlreadyExists):
    return JSONResponse(
        status_code=400,
        content={'message': f'{exc.message}'}
    )
