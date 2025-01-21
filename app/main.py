from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from app.core import settings, db_helper



@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

    await db_helper.dispose()


app = FastAPI(lifespan=lifespan)

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        port = settings.PORT,
        host = settings.HOST
    )