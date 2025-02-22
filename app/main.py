from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from app.api import router
from app.core import settings, db_helper
from app.exceptions import UserNotFoundException, user_not_found_exception_handler, user_already_exists_handler, \
    UserAlreadyExistsException


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

    await db_helper.dispose()


app = FastAPI(lifespan=lifespan)

app.add_exception_handler(UserNotFoundException, user_not_found_exception_handler)
app.add_exception_handler(UserAlreadyExistsException, user_already_exists_handler)
app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        port = settings.PORT,
        host = settings.HOST
    )