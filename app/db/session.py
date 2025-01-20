from sqlalchemy.ext.asyncio import async_sessionmaker



async_session = async_sessionmaker()




async def get_session():
    async with async_session() as session:
        yield session