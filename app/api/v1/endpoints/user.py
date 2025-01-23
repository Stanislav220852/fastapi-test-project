from fastapi import APIRouter
from app.schemas.schemas import UserSchem
from app.services.user_service import UserServises


user_router = APIRouter(prefix='/users',tags=["users"])

@user_router.post("/add")
async def add_users(schem:UserSchem):
    return await UserServises.create_user(schem)

@user_router.get("/get_users")
async def get_user():
    return await UserServises.get_users()
