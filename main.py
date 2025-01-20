from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.db.base import create_table
import uvicorn
@asynccontextmanager
async def lifspan(app:FastAPI):
    await create_table()
    print('база создана')
    yield
    print('База очищена')

app = FastAPI(lifespan=lifspan)


if __name__ == "__main__":
    uvicorn.run("main:app",reload=True)


