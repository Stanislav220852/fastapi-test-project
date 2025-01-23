from sqlalchemy import select
from app.db.session import async_session
from app.models.model import UserModel
from app.schemas.schemas import UserSchem
from app.core.hash_pass import hash_password
from fastapi import HTTPException


class UserServises:
    @classmethod
    async def create_user(cls,user:UserSchem):
        async with async_session() as session:
            user_in = user.model_dump()
            model = UserModel(**user_in)
            model.password = await hash_password(model.password)
            
            session.add(model)
            await session.commit()
            return model
        
    @classmethod
    async def get_users(cls):
        async with async_session() as session:
            model = select(UserModel).order_by(UserModel.id)
            result = await session.execute(model)
            users = result.scalars().all()
            if not users:
                raise HTTPException(status_code=404,detail="Not found users")
            await session.commit()
            return users