from sqlalchemy.ext.asyncio import async_sessionmaker
from app.db.base import engine


async_session = async_sessionmaker(engine,expire_on_commit=False)


async def get_session():
    async with async_session() as session:
        yield session