from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.db.base import create_table
import uvicorn
from app.api.v1.endpoints.user import user_router


@asynccontextmanager
async def lifspan(app:FastAPI):
    await create_table()
    print('база создана')
    yield
    print('База очищена')

app = FastAPI(lifespan=lifspan)

app.include_router(user_router)

if __name__ == "__main__":
    uvicorn.run("main:app",reload=True)


