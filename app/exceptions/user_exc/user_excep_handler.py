from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.responses import Response

from app.exceptions.user_exc.user_excep import UserNotFoundException, UserAlreadyExistsException


async def user_not_found_exception_handler(request: Request, exc: UserNotFoundException) -> Response:
    return JSONResponse(
        status_code=404,
        content={'message': f'{exc.message}'}
    )

async def user_already_exists_handler(request: Request, exc: UserAlreadyExistsException):
    return JSONResponse(
        status_code=400,
        content={'message': f'{exc.message}'}
    )


