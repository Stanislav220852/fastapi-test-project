from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ALGORITHM: str = "HS256"
    SECRET_KEY:str = "SECRET_KEY"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 720
    API_PORT:int = 8000
    DEBAG:bool = True
    DATABASE_URL = "postgresql+asyncpg://postgres:1111@localhost:5432/todo"
    

    class Config:
        env_file = ".env"
        env_file_encofing = "utf-8"


        

settings = Settings()